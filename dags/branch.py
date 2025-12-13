from airflow.sdk import dag,task

@dag
def branch():

        @task
        def a():
                return 1
        @task.branch
        def b(val):
                if val==1:
                        return ["equal_to_1","different_one"]
                return "not_equal_to_1"
        @task
        def equal_to_1(val:int):
                print(f'Equal to 1 {val}')
        @task
        def not_equal_to_1(val:int):
                print(f'Not equal to 1 {val}')
        @task
        def different_one(val:int):
                print(f"Someting else {val}")

        val = a()
        b(val) >> [equal_to_1(val),not_equal_to_1(val),different_one(val)]

branch()