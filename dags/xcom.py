from airflow.sdk import task,dag,Context

@dag
def my_dag():

        @task
        def t1() ->int:
                val = 42
                return val

        @task
        def t2(val : int):
                print(val)

        val = t1() 
        t2(val)

my_dag()