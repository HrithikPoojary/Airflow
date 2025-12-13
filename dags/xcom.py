from airflow.sdk import task,dag
from typing import Dict,Any

@dag
def my_dag():

        @task
        def t1() ->Dict[str,Any]:
                val = 42
                my_sentenct = "Hello World"
                return {
                        "val" : val,
                        "my_sentence" : my_sentenct
                        }

        @task
        def t2(data : Dict[str,Any]):
                print(data['val'])
                print(data['my_sentence'])

        values = t1() 
        t2(values)

my_dag()