from airflow.sdk import dag,task,task_group

@dag
def group():

        @task
        def A():
                return 42

        @task_group(
                        default_args={
                                "retries":2
                        }
        )
        def my_group(val : int):
                @task
                def B(my_val : int):
                        return my_val + 42
                
                @task_group(
                                default_args={
                                        "retries":3
                                }
                )
                def my_nested_group():
                        @task
                        def C():
                                print("C")
                        C()

                B(val) >> my_nested_group()

        val = A() 
        my_group(val)
group() 