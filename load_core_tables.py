import pandas as pd
import pyodbc
import os



SERVER = "localhost,1433"
DATABASE = "EcommerceDW"
USERNAME = "sa"
PASSWORD = "Thuande@2026SQL"

RAW_PATH = "data/raw"




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




def load_dataframe(df, table_name, create_sql, insert_sql):

    print(f"\n===== {table_name.upper()} =====")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    # Drop table if exists
    cursor.execute(f"""
        IF OBJECT_ID('bronze.{table_name}', 'U') IS NOT NULL
            DROP TABLE bronze.{table_name};
    """)

    cursor.execute(create_sql)
    conn.commit()

    print(" Bronze table created")

    # Convert NaN -> None
    df = df.where(pd.notnull(df), None)

    # Insert
    cursor.fast_executemany = True

    cursor.executemany(
        insert_sql,
        df.itertuples(index=False, name=None)
    )

    conn.commit()

    print(" Data loaded")



customers = pd.read_csv(
    os.path.join(
        RAW_PATH,
        "olist_customers_dataset.csv"
    )
)

customers_sql = """
CREATE TABLE bronze.olist_customers
(
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);
"""

customers_insert = """
INSERT INTO bronze.olist_customers
(
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
)
VALUES (?, ?, ?, ?, ?)
"""

load_dataframe(
    customers,
    "olist_customers",
    customers_sql,
    customers_insert
)



order_items = pd.read_csv(
    os.path.join(
        RAW_PATH,
        "olist_order_items_dataset.csv"
    )
)

order_items_sql = """
CREATE TABLE bronze.olist_order_items
(
    order_id VARCHAR(50),
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME2,
    price DECIMAL(18,2),
    freight_value DECIMAL(18,2)
);
"""

order_items_insert = """
INSERT INTO bronze.olist_order_items
(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

load_dataframe(
    order_items,
    "olist_order_items",
    order_items_sql,
    order_items_insert
)




products = pd.read_csv(
    os.path.join(
        RAW_PATH,
        "olist_products_dataset.csv"
    )
)

products_sql = """
CREATE TABLE bronze.olist_products
(
    product_id VARCHAR(50),
    product_category_name VARCHAR(100),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g DECIMAL(18,2),
    product_length_cm DECIMAL(18,2),
    product_height_cm DECIMAL(18,2),
    product_width_cm DECIMAL(18,2)
);
"""

products_insert = """
INSERT INTO bronze.olist_products
(
    product_id,
    product_category_name,
    product_name_length,
    product_description_length,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

load_dataframe(
    products,
    "olist_products",
    products_sql,
    products_insert
)



print("\n========== FINAL CHECK ==========")

for table in [
    "olist_customers",
    "olist_order_items",
    "olist_products"
]:

    cursor.execute(
        f"SELECT COUNT(*) FROM bronze.{table}"
    )

    count = cursor.fetchone()[0]

    print(f"bronze.{table}: {count:,} rows")


cursor.close()
conn.close()

print("\n CORE ETL COMPLETED!")