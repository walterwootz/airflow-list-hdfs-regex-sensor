# Apache Airflow ListHDFSRegexSensor
Class extension of Airflow [HdfsRegexSensor](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/_modules/airflow/providers/apache/hdfs/sensors/hdfs.html#HdfsRegexSensor) to save in a xcom variable the list of recognized objects.
When sensor recognize the pattern in the regex, it save the list in a Xcom variable called `files`, but you can change it as you prefer.

## Requirements
- [Apache Airflow](https://airflow.apache.org/) >= 2.5.1
- [apache-airflow-providers-apache-hdfs](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html) (>=3.2.0) installed on airflow

## How to use it
Include the definition of the class in your project (for example inside a DAG) and define a new task using the new sensor. An example is provided.