import requests
from os import getcwd
from pathlib import Path
import yaml

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yaml") as f:
    api_vars = yaml.safe_load(f)['api']

if api_vars['apiName'] == 'apidae':

    url = api_vars['url']
    projectId = api_vars['projectId']
    searchId = api_vars['searchId']
    count = api_vars['count']
    apiKey = api_vars['apiKey']
    typeObjet = api_vars['typeObjet']

    print(f"HTTP GET to {api_vars['apiName']}: {api_vars['url']}")

    query = f'"projetId":"{projectId}","apiKey":"{apiKey}","selectionIds":[{searchId}],"criteresQuery":"type:{typeObjet}","count":"{count}"'
    url = f'{url}?query=' + '{' + query + '}'

    r = requests.get(url)
    response = r.json()

elif api_vars['apiName'] == 'datatourisme':
    url = api_vars['url']

    response = requests.get(url)
    response = response.content

elif api_vars['apiName'] == 'local':

    with open(f'{parent_path}/data/{api_vars["file"]}') as f:
        response = f.read()

else:
    print('No API found.')
