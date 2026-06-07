from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator 
from datetime import datetime


with DAG(
    'extract',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    test_task = SQLExecuteQueryOperator(
        task_id='extract_json',
        conn_id='my_postgres_conn',
        sql="""
        create table if not exists extract_demo.data_from_json as
        select 
	        pet->>'name' as name,
	        pet->>'species' as species,
	        pet->>'birthYear' as birthYear,
	        pet->>'photo' as photo
        from extract_demo.json_content,
        jsonb_array_elements(json_data->'pets') as pet;
        """
    )
