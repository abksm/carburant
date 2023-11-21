import requests
from datetime import datetime
import json
import psycopg2

conn = psycopg2.connect(
    database="carburants",
    user="yzpt",
    password="yzpt",
    host="localhost",
    port="5432"
)

def extract_data():
    limit = 3
    url = f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?limit={limit}&timezone=Europe%2FParis"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # save into json file
        with open(f"data/carburants_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            f.write(json.dumps(data['results'], indent=4))

        for result in data['results']:
            # line example: {
            #     "id": 68200004,
            #     "latitude": "4773900",
            #     "longitude": 729200.0,
            #     "cp": "68200",
            #     "pop": "R",
            #     "adresse": "258 RUE DE BELFORT",
            #     "ville": "Mulhouse",
            #     "horaires": "{\"@automate-24-24\": \"1\", \"jour\": [{\"@id\": \"1\", \"@nom\": \"Lundi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"20.00\"}}, {\"@id\": \"2\", \"@nom\": \"Mardi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"20.00\"}}, {\"@id\": \"3\", \"@nom\": \"Mercredi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"20.00\"}}, {\"@id\": \"4\", \"@nom\": \"Jeudi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"20.00\"}}, {\"@id\": \"5\", \"@nom\": \"Vendredi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"20.00\"}}, {\"@id\": \"6\", \"@nom\": \"Samedi\", \"@ferme\": \"\", \"horaire\": {\"@ouverture\": \"08.30\", \"@fermeture\": \"19.00\"}}, {\"@id\": \"7\", \"@nom\": \"Dimanche\", \"@ferme\": \"1\"}]}",
            #     "services": "{\"service\": [\"Station de gonflage\", \"Vente de gaz domestique (Butane, Propane)\", \"Automate CB 24/24\", \"DAB (Distributeur automatique de billets)\"]}",
            #     "prix": "[{\"@nom\": \"Gazole\", \"@id\": \"1\", \"@maj\": \"2023-11-21 07:10:36\", \"@valeur\": \"1.829\"}, {\"@nom\": \"E85\", \"@id\": \"3\", \"@maj\": \"2023-11-21 07:10:36\", \"@valeur\": \"0.994\"}, {\"@nom\": \"GPLc\", \"@id\": \"4\", \"@maj\": \"2023-11-21 07:10:36\", \"@valeur\": \"1.050\"}, {\"@nom\": \"E10\", \"@id\": \"5\", \"@maj\": \"2023-11-21 07:10:36\", \"@valeur\": \"1.825\"}, {\"@nom\": \"SP98\", \"@id\": \"6\", \"@maj\": \"2023-11-21 07:10:36\", \"@valeur\": \"1.899\"}]",
            #     "geom": {
            #         "lon": 7.292,
            #         "lat": 47.739
            #     },
            #     "gazole_maj": "2023-11-21 07:10:36",
            #     "gazole_prix": "1.829",
            #     "sp95_maj": null,
            #     "sp95_prix": null,
            #     "e85_maj": "2023-11-21 07:10:36",
            #     "e85_prix": "0.994",
            #     "gplc_maj": "2023-11-21 07:10:36",
            #     "gplc_prix": "1.050",
            #     "e10_maj": "2023-11-21 07:10:36",
            #     "e10_prix": "1.825",
            #     "sp98_maj": "2023-11-21 07:10:36",
            #     "sp98_prix": "1.899",
            #     "carburants_disponibles": [
            #         "Gazole",
            #         "E85",
            #         "GPLc",
            #         "E10",
            #         "SP98"
            #     ],
            #     "carburants_indisponibles": [
            #         "SP95"
            #     ],
            #     "horaires_automate_24_24": "Oui",
            #     "services_service": [
            #         "Station de gonflage",
            #         "Vente de gaz domestique (Butane, Propane)",
            #         "Automate CB 24/24",
            #         "DAB (Distributeur automatique de billets)"
            #     ],
            #     "departement": "Haut-Rhin",
            #     "code_departement": "68",
            #     "region": "Grand Est",
            #     "code_region": "44"
            # }
            line = {}
            line['id']              = result['id']
            line['cp']              = result['cp']
            line['pop']             = result['pop']
            line['adresse']         = result['adresse']
            line['ville']           = result['ville']
            line['horaires']        = result['horaires']
            line['services']        = result['services']
            line['prix']            = result['prix']
            line['longitude']       = result['geom']['lon']
            line['latitude']        = result['geom']['lat']
            line['gazole_maj']      = result['gazole_maj']
            line['gazole_prix']     = result['gazole_prix']
            line['sp95_maj']        = result['sp95_maj']
            line['sp95_prix']       = result['sp95_prix']
            line['e85_maj']         = result['e85_maj']
            

            


    else:
        print('error')
        raise Exception(f"Error: {response.status_code}")
    

if __name__ == "__main__":

    extract_data()