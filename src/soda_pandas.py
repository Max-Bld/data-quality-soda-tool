##
import pandas as pd
import dask
import dask.dataframe as dd
import json
from soda.scan import Scan
from http_request import response
from functions import get_values
from os import getcwd
from pathlib import Path
import yaml
# from flatten_json import flatten_preserve_lists
import io

dask.config.set({"dataframe.convert-string": False})


## vars

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yml") as f:
    backend_vars = yaml.safe_load(f)['backend']
with open(f"{parent_path}/config/variables.yml") as f:
    soda_vars = yaml.safe_load(f)['soda']
with open(f"{parent_path}/config/variables.yml") as f:
    api_vars = yaml.safe_load(f)['api']

## backend script

data = response

with open(f'{parent_path}/criteria/{backend_vars["criteria"]}') as json_file:
    criteria = json.load(json_file)

    # json

if api_vars['content-type'] == "application/json":

    data = data['objetsTouristiques']
    results = get_values(data, criteria)
    df = dd.DataFrame.from_dict(results, npartitions=4) # dask
    # data = flatten_preserve_lists({"data":data})
    # df = pd.DataFrame.from_dict(data) # pandas
    print(df.columns)
    print(len(df.columns))
    print(df)
    print(df['nom'])

    # csv

elif api_vars['content-type'] == "text/csv":

    cols = []
    for n in criteria:
        cols.append(criteria[n][0])

    if api_vars['apiName'] == "local":
        # df = pd.read_csv(f'{parent_path}/data/{api_vars["file"]}', usecols=cols) # pandas
        df = dd.read_csv(f'{parent_path}/data/{api_vars["file"]}', usecols=cols) # dask

    else:
        df = pd.read_csv(io.StringIO(data.decode('utf-8')), usecols=cols) # pandas
        df = dd.from_pandas(df, npartitions=4) # dask

    for n in criteria:
        df = df.rename(columns={criteria[n][0]: n})

## Soda
print("Starting Soda Scan.")
scan = Scan()

# add Pandas dataframe to scan and assign a dataset name to refer from checks.yaml
# scan.add_pandas_dataframe(dataset_name=soda_vars['dataset_name'], pandas_df=df, data_source_name=soda_vars['data_source_name']) # pandas
scan.add_dask_dataframe(dataset_name=soda_vars['dataset_name'], dask_df=df, data_source_name=soda_vars['data_source_name']) # dask

# Set the scan definition name and default data source to use
scan.set_scan_definition_name(soda_vars['scan_definition_name'])
scan.set_data_source_name(soda_vars['data_source_name'])

# Define checks in yaml format
scan.add_sodacl_yaml_file(file_path=f"{parent_path}/config/checks.yml")

scan.execute()
scan.set_verbose(True)
result = scan.get_scan_results()
result['logs'][2]['message'] = result['logs'][2]['message'].replace("'", "")
j = json.dumps(result)

print("Soda Scan finished.")