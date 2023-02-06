# Apache Airflow ListHdfsRegexSensor
Class extension of Airflow [HdfsRegexSensor](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/_modules/airflow/providers/apache/hdfs/sensors/hdfs.html#HdfsRegexSensor) to save in a Xcom variable the list of recognized objects.
When sensor recognizes the pattern in the regex, it saves the list in a Xcom json array variable called `files`, but you can change it as you prefer.

## Requirements
- [Apache Airflow](https://airflow.apache.org/) >= 2.5.1
- [apache-airflow-providers-apache-hdfs](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html) (>=3.2.0) installed on airflow

## How to use it
Import the definition of the class in your project (for example inside a DAG) and define a new task using the new sensor. An example is provided in the folder [example](./example).
