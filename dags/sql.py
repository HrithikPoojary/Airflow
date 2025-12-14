from airflow.sdk import task,dag

@dag
def sql_dag():

        @task.sql(
                conn_id = 'postgres'
        )
        def get_nb_xcoms():
                return "select count(*) from xcom"
        
        get_nb_xcoms()

sql_dag()

# docker compose up --build