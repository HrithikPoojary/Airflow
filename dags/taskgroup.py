from airflow.sdk import dag,task,task_group

@dag
def group():

        @task
        def A():
                print("A")

        @task_group(
                        default_args={
                                "retries":2
                        }
        )
        def my_group():
                @task
                def B():
                        print("B")
                
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

                B() >> my_nested_group()

        A()>> my_group()
group() 