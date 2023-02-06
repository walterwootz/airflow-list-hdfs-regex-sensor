from airflow.providers.apache.hdfs.sensors.hdfs import HdfsRegexSensor

class ListHdfsRegexSensor(HdfsRegexSensor):
    def poke(self, context):
        sb_client = self.hook(self.hdfs_conn_id).get_conn()
        self.log.info(
            "Poking for %s to be a directory with files matching %s", self.filepath, self.regex.pattern
        )
        result = [
            f
            for f in sb_client.ls([self.filepath], include_toplevel=False)
            if f["file_type"] == "f" and self.regex.match(f["path"].replace(f"{self.filepath}/", ""))
        ]
        result = self.filter_for_ignored_ext(result, self.ignored_ext, self.ignore_copying)
        result = self.filter_for_filesize(result, self.file_size)
        context['ti'].xcom_push('files', result)
        return bool(result)