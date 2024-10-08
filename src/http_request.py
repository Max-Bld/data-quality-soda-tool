import requests
from os import getcwd
from pathlib import Path
import yaml

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/variables.yaml") as f:
    api_vars = yaml.safe_load(f)['api']

url = api_vars['url']
projectId = api_vars['projectId']
searchId = api_vars['searchId']
count = api_vars['count']
apiKey = api_vars['apiKey']
typeObjet = api_vars['typeObjet']

query = f'"projetId":"{projectId}","apiKey":"{apiKey}","selectionIds":[{searchId}],"criteresQuery":"type:{typeObjet}","count":"{count}"'
url = f'{url}?query=' + '{' + query + '}'

r = requests.get(url)

response = r.json()