# Airflow

Postgres Connection
SQLExecuteQueryOperator(task_id = '',
conn_id = 'postgres', ->  This should match with airflow UI->Admin->Connections->Connection ID
sql = '''
DML OR DDL
''')
Connection ID -> postgres
Connection Type ->postgres   --If No desired result then download it from astronomer.io
Desciption -> Optional
Host ->postgres
Login ->airflow
Password ->airflow
Post ->5432
