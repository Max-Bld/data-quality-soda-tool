import psycopg2
from soda_pandas import j
from os import getcwd
from pathlib import Path
import yaml

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yaml") as f:
    psql_vars = yaml.safe_load(f)['postgresql']

conn = psycopg2.connect(
    database=psql_vars['database'], user=psql_vars['user'], password=psql_vars['password'], host=psql_vars['host'], port=psql_vars['port']
)
conn.autocommit = True
cursor = conn.cursor()

print("Starting INSERT into PostgresSQL database:")

print(f'''INSERT INTO {psql_vars['table']}({psql_vars['column']}) VALUES ('{j}')''')
cursor.execute(f'''INSERT INTO {psql_vars['table']}({psql_vars['column']}) VALUES ('{j}')''')

print('Insert in PostgresSQL database finished.')

cursor.close()
conn.close()