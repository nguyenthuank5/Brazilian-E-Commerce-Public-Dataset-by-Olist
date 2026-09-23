from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="ecommerce_data_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ecommerce", "etl", "data-engineering"],
) as dag:

    load_orders = BashOperator(
        task_id="load_orders",
        bash_command="python /opt/airflow/project/src/load_orders.py",
    )

    load_core_tables = BashOperator(
        task_id="load_core_tables",
        bash_command="python /opt/airflow/project/src/load_core_tables.py",
    )

    load_orders >> load_core_tables