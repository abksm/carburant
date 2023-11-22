import requests
from datetime import datetime
import psycopg2
import json

conn = psycopg2.connect(
    database="carburants",
    user="yzpt",
    password="yzpt",
    host="localhost",
    port="5432"
)

def extract_data():
    # limit = 3
    url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?timezone=Europe%2FParis"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        record_timestamp = datetime.now()
        # save into json file
        with open(f"carburants_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            f.write(json.dumps(data['results'], indent=4))

        cur = conn.cursor()

        for result in data['results']:
            fields = result
            fields['record_timestamp'] = record_timestamp
            sql = """
            INSERT INTO raw_fields (
                id, cp, pop, adresse, ville, horaires, services, latitude, longitude, gazole_maj, gazole_prix, sp95_maj, sp95_prix, e85_maj, e85_prix, gplc_maj, gplc_prix, e10_maj, e10_prix, sp98_maj, sp98_prix, carburants_disponibles, carburants_indisponibles, horaires_automate_24_24, departement, code_departement, region, code_region, record_timestamp
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """

            cur.execute(sql, (
                fields.get('id'), 
                fields.get('cp'),
                fields.get('pop'),
                fields.get('adresse'),
                fields.get('ville'),
                fields.get('horaires'), 
                fields.get('services_service'), 
                fields['geom'].get('lon'), 
                fields['geom'].get('lat'),
                fields.get('gazole_maj'), 
                fields.get('gazole_prix'), 
                fields.get('sp95_maj'), 
                fields.get('sp95_prix'), 
                fields.get('e85_maj'), 
                fields.get('e85_prix'), 
                fields.get('gplc_maj'), 
                fields.get('gplc_prix'), 
                fields.get('e10_maj'), 
                fields.get('e10_prix'), 
                fields.get('sp98_maj'), 
                fields.get('sp98_prix'), 
                fields.get('carburants_disponibles'), 
                fields.get('carburants_indisponibles'), 
                fields.get('horaires_automate_24_24'), 
                fields.get('departement'), 
                fields.get('code_departement'), 
                fields.get('region'), 
                fields.get('code_region'),
                fields.get('record_timestamp')
            ))

        conn.commit()
        

    else:
        print('error')
        raise Exception(f"Error: {response.status_code}")
    

if __name__ == "__main__":
    extract_data()