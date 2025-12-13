from airflow.sdk import dag,task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sdk.bases.sensor import PokeReturnValue
from airflow.providers.postgres.hooks.postgres import PostgresHook



# from airflow.providers.standard.operators.python import PythonOperator
# def _extract_user(ti):
#         # fake_user = ti.xcom_pull(task_ids="is_api_available")  # Will get this result from return PokeReturnValue(is_done=condition,xcom_value=fake_user)
#         # For Testing
#         import requests
#         response = requests.get("https://raw.githubusercontent.com/marclamberti/datasets/refs/heads/main/fakeuser.json")
#         fake_user = response.json()
#         return {
#                 "id" : fake_user['id'],
#                 "firstName" : fake_user['personalInfo']['firstName'],
#                 "lastName" : fake_user['personalInfo']['lastName'],
#                 "email" : fake_user['personalInfo']['email']
#         }


@dag
def user_processing():     # DAG name

        create_table = SQLExecuteQueryOperator(      #First Task
                task_id = "create_table",
                conn_id = "postgres",
                sql = '''
                        create table if not exists users(
                        id int primary key ,
                        firstName varchar(255),
                        lastName varchar(255),
                        email varchar(255),
                        created_at timestamp default current_timestamp
                        )
                        '''
        )

        @task.sensor(poke_interval=30 ,timeout= 300)
        def is_api_available() -> PokeReturnValue:
                import requests
                response = requests.get("https://raw.githubusercontent.com/marclamberti/datasets/refs/heads/main/fakeuser.json")
                print(response.status_code)

                if response.status_code == 200:
                        condition = True
                        fake_user = response.json()
                else:
                        condition = False
                        fake_user = None
                return PokeReturnValue(is_done=condition,xcom_value=fake_user)  # For sensor we have to return Pokereturn value
        
        @task
        def extract_user(fake_user):
                return {
                        "id" : fake_user['id'],
                        "firstName" : fake_user['personalInfo']['firstName'],
                        "lastName" : fake_user['personalInfo']['lastName'],
                        "email" : fake_user['personalInfo']['email']
                }

        @task
        def process_user(user_info):
                import csv
                from datetime import datetime
                user_info["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("/tmp/user_info.csv",mode='w',newline="") as f:
                        writer = csv.DictWriter(f,fieldnames=user_info.keys())
                        writer.writeheader()
                        writer.writerow(user_info)
        @task 
        def store_user():
                hook = PostgresHook(postgres_conn_id = "postgres")
                hook.copy_expert(
                        sql="copy users from stdin with csv header",
                        filename="/tmp/user_info.csv"
                )
                
        fake_user = is_api_available()
        user_info = extract_user(fake_user)
        process_users = process_user(user_info)

        create_table >> fake_user >> user_info >> process_users >> store_user()

user_processing()