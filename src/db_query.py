import psycopg2
from pprint import pprint
import json
from os import getcwd
from pathlib import Path
import yaml

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yml") as f:
    psql_vars = yaml.safe_load(f)['postgresql']

def get_last_results():
    conn = psycopg2.connect(
        database=psql_vars['database'], user=psql_vars['user'], password=psql_vars['password'], host=psql_vars['host'], port=psql_vars['port']
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM soda_results''')
    results = cursor.fetchall()[-1][0]
    cursor.close()
    conn.close()

    return results
