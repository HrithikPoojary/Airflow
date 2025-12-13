from airflow.sdk import task,dag
from time import sleep

@dag
def celery_dag():
        @task
        def A():
                sleep(5)
        
        @task
        def B():
                sleep(5)

        @task
        def C():
                sleep(5)

        @task
        def D():
                sleep(5)

        A()>>[B(),C()]>>D()

celery_dag()