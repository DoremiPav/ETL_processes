FROM apache/airflow:3.1.7

# переключаемся на airflow пользователя
USER airflow

# ставим Postgres provider
RUN pip install --no-cache-dir apache-airflow-providers-postgres