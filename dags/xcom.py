from airflow.sdk import task,dag,Context

@dag
def my_dag():

        @task
        def t1(context : Context):
                val = 42
                context['ti'].xcom_push(key='my_key',value= val)

        @task
        def t2(context :Context):
                val = context['ti'].xcom_pull(task_ids='t1',key='my_key')
                print(val)

        t1() >>t2()

my_dag()