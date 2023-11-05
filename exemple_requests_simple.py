import requests

# Spécifiez l'URL du point d'API avec lequel vous souhaitez interagir
url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?limit=3&timezone=Europe%2FParis"

# Effectuez une requête GET vers l'URL spécifiée
response = requests.get(url)

# Vérifiez si la requête a été réussie (code d'état HTTP 200)
if response.status_code == 200:
    # Analysez la réponse JSON de l'API
    data = response.json()
    # Affichez les données de la réponse
    print("Données de la réponse :")
    print(data)


    # Maintenant ici, se démerder pour enregistrer les données dans un fichier JSON, et un fichier csv
    # ...


else:
    # Affichez un message d'erreur si la requête n'a pas réussi
    print(f"Erreur : Impossible de récupérer les données de l'API (Code d'état : {response.status_code})")
