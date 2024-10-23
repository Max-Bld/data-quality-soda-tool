import psycopg2
from soda_pandas import get_soda_results
from os import getcwd
from pathlib import Path
import yaml
from elastic import send_to_elastic

## vars

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yml") as f:
    backend_vars = yaml.safe_load(f)['backend']
with open(f"{parent_path}/config/variables.yml") as f:
    soda_vars = yaml.safe_load(f)['soda']
with open(f"{parent_path}/config/variables.yml") as f:
    api_vars = yaml.safe_load(f)['api']

## http request

from http_request import get_response

response = get_response(api_vars)

## soda results

import pandas as pd
import dask
import dask.dataframe as dd
import json
from soda.scan import Scan
from functions import get_values
from os import getcwd
from pathlib import Path
import yaml
# from flatten_json import flatten_preserve_lists
import io

dask.config.set({"dataframe.convert-string": False})




## backend script

data = response

with open(f'{parent_path}/criteria/{backend_vars["criteria"]}') as json_file:
    criteria = json.load(json_file)

j = get_soda_results(data, criteria, api_vars, soda_vars, parent_path)

## Database insert

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yml") as f:
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

## Send to Elastic

send_to_elastic()