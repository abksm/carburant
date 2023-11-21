import requests
import json
import csv

api_url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records"

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Erreur lors de la requête à l'API. Code de statut :", response.status_code)
            return None
    except Exception as e:
        print("Erreur :", e)
        return None

def save_as_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Données enregistrées au format JSON dans le fichier : {filename}")

def save_as_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(data[0].keys())
        
        for item in data:
            csv_writer.writerow(item.values())
    print(f"Données enregistrées au format CSV dans le fichier : {filename}")

if __name__ == "__main__":
    api_data = fetch_data(api_url)
    
    if api_data:
        save_as_json(api_data, "data.json")
        
        save_as_csv(api_data, "data.csv")