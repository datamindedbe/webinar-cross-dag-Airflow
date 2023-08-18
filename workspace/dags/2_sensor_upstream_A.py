from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.external_task_marker import ExternalTaskMarker

# DAG for upstream_dag_A
with DAG(
    "upstream_dag_A",
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    start_task_A = BashOperator(
        task_id="start_task_A",
        bash_command="echo 'Start task in upstream_dag_A'",
    )
    
    end_task_A_marker = ExternalTaskMarker(
        task_id="end_task_A_marker",
        external_dag_id="downstream_sensor_dag",
        external_task_id="sensor_A",
    )
    
    start_task_A >> end_task_A_marker