# Configuring Airflow

```
$ mkdir -p ./dags ./logs ./plugins ./config
$ export AIRFLOW_UID=50000
$ chown $AIRFLOW_UID:$AIRFLOW_UID dags logs plugins config
$ docker compose up airflow-init
$ docker compose up
```

Cleanup:

```
$ docker compose down --volumes --remove-orphans
```

More info: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/
