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
            f.write(json.dumps(data, indent=4))

        print("allo ok")

    else:
        print('error')
        raise Exception(f"Error: {response.status_code}")
    

if __name__ == "__main__":

    extract_data()