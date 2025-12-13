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
                
                @task
                def C():
                        print("C")

                B() >> C()

        A()>> my_group()
group() 