from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
        print("Primeira Dag")
              
with DAG(dag_id="Primeira_dag_Airflow",
         start_date=datetime(2024,3,24),
         schedule_interval="* * * * *",
         catchup=False) as dag:
    

    task1 = PythonOperator(
            task_id="Primeira Dag",
            python_callable=helloWorld)