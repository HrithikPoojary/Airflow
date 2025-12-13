from airflow.sdk import dag,task,task_group

@dag
def group():

        @task
        def A():
                print("A")

        @task_group
        def my_group():
                @task
                def B():
                        print("B")
                
                @task_group
                def my_nested_group():
                        @task
                        def C():
                                print("C")
                        C()

                B() >> my_nested_group()

        A()>> my_group()
group() 