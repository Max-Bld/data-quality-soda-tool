##
import pandas as pd
import json
from soda.scan import Scan
from http_request import response
from functions import compute_completeness, get_values
from os import getcwd
from pathlib import Path

data = response

parent_path = Path(getcwd()).parent.absolute()

with open(f'{parent_path}/data/criteria.json') as json_file:
    criteria = json.load(json_file)

restauration = data['objetsTouristiques']

results = get_values(restauration, criteria)

df = pd.DataFrame.from_dict(results)

## Soda

scan = Scan()

# add Pandas dataframe to scan and assign a dataset name to refer from checks.yaml
scan.add_pandas_dataframe(dataset_name="restauration", pandas_df=df, data_source_name="apidae")

# Set the scan definition name and default data source to use
scan.set_scan_definition_name("test")
scan.set_data_source_name("apidae")

# Add configuration YAML file
# You do not need connection to a data source; you must have a connection to Soda Cloud
scan.add_configuration_yaml_file(file_path=f"{parent_path}/config/configuration.yml")

# Define checks in yaml format
scan.add_sodacl_yaml_file(file_path=f"{parent_path}/config/checks.yml")

scan.execute()
scan.set_verbose(True)
result = scan.get_scan_results()
result['logs'][2]['message'] = result['logs'][2]['message'].replace("'", "")
j = json.dumps(result)

## to Retool
#r = requests.post('https://api.retool.com/v1/workflows/6721da9b-b325-4a06-b05f-83781bb5024d/startTrigger', headers = {"X-Workflow-Api-Key": "retool_wk_93464b978966477ba6a7b6eb77a1b0c7"}, data=j)