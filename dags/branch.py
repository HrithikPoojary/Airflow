from airflow.sdk import dag,task

@dag
def branch():

        @task
        def a():
                return 1
        @task.branch
        def b(val):
                if val==1:
                        return "equal_to_1"
                return "not_equal_to_1"
        @task
        def equal_to_1():
                print('Equal to 1')
        @task
        def not_equal_to_1():
                print('Not equal to 1')

        val = a()
        b(val) >> [equal_to_1(),not_equal_to_1()]

branch()