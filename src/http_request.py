import requests

url = "https://api.apidae-tourisme.cooking/api/v002/recherche/list-objets-touristiques"
projectId = "3628"
searchId = "69700"
count = "20"
apiKey = "8uEnYKe1"
typeObjet = "RESTAURATION"

query = f'"projetId":"{projectId}","apiKey":"{apiKey}","selectionIds":[{searchId}],"criteresQuery":"type:{typeObjet}","count":"{count}"'
url = f'{url}?query=' + '{' + query + '}'

r = requests.get(url)

response = r.json()