import pandas as pd
import pyodbc


SERVER = "sqlserver-de,1433"
DATABASE = "EcommerceDW"
USERNAME = "sa"
PASSWORD = "Thuande@2026SQL"

FILE_PATH = "data/raw/olist_orders_dataset.csv"



connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

print(" Connected to SQL Server")




df = pd.read_csv(FILE_PATH)

print("\n===== EXTRACT =====")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())



print("\n===== VALIDATION =====")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())



cursor.execute("""
IF OBJECT_ID('bronze.olist_orders', 'U') IS NOT NULL
    DROP TABLE bronze.olist_orders;
""")

cursor.execute("""
CREATE TABLE bronze.olist_orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp DATETIME2,
    order_approved_at DATETIME2 NULL,
    order_delivered_carrier_date DATETIME2 NULL,
    order_delivered_customer_date DATETIME2 NULL,
    order_estimated_delivery_date DATETIME2
);
""")

conn.commit()

print("\n Bronze table created")



date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")




insert_query = """
INSERT INTO bronze.olist_orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in df.itertuples(index=False, name=None):
    cursor.execute(insert_query, row)

conn.commit()

print(" Data loaded into bronze.olist_orders")




cursor.execute("""
SELECT COUNT(*)
FROM bronze.olist_orders;
""")

count = cursor.fetchone()[0]

print(f"\nRows in SQL Server: {count}")


cursor.close()
conn.close()

print("\n ETL completed successfully")