import airflow
from airflow.models import DAG
import re
from list_hdfs_regex_sensor import ListHdfsRegexSensor
from airflow.operators.python import PythonOperator

args = {
    'owner': 'owner',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='list-hdfs-example',
    default_args=args,
    schedule_interval=None
)

# Define task A as our Sensor
A = ListHdfsRegexSensor(
    task_id="list_hdfs_regex_sensor",
    filepath='/input',
    hdfs_conn_id='webhdfs_default',
    regex=re.compile('.*\.png'),
    dag=dag
)

# Define task B as example that pull file list from Xcom and print it
def task_B(**kwargs):
    print('Task B starting...')
    files = kwargs['ti'].xcom_pull(task_ids='list_hdfs_regex_sensor', key='files')
    print(files)
    return True

B = PythonOperator(
    task_id='task_B',
    python_callable=task_B,
    provide_context=True,
    dag=dag
)

A >> B
