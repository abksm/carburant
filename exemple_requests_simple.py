import requests

url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?limit=3&timezone=Europe%2FParis"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)