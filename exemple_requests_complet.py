# Bien sûr, voici un exemple de script Python qui effectue une requête à une API, 
# stocke les données au format JSON et CSV, avec des commentaires expliquant chaque 
# étape du processus. 

# Assurez-vous d'avoir le module requests installé en exécutant 
# pip install requests 
# avant d'exécuter le script.

# Importation des bibliothèques nécessaires
import requests
import json
import csv

# URL de l'API à requêter
api_url = "https://api.exemple.com/data"

# Fonction pour effectuer la requête à l'API
def fetch_data(api_url):
    try:
        # Faire la requête à l'API
        response = requests.get(api_url)
        
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Charger les données JSON à partir de la réponse
            data = response.json()
            return data
        else:
            # Si la requête échoue, afficher un message d'erreur
            print("Erreur lors de la requête à l'API. Code de statut :", response.status_code)
            return None
    except Exception as e:
        # En cas d'erreur, afficher l'erreur
        print("Erreur :", e)
        return None

# Fonction pour enregistrer les données au format JSON
def save_as_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Données enregistrées au format JSON dans le fichier : {filename}")

# Fonction pour enregistrer les données au format CSV
def save_as_csv(data, filename):
    # Ouvrir le fichier CSV en mode écriture
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        # Créer un objet writer CSV
        csv_writer = csv.writer(csv_file)
        
        # Écrire l'en-tête du fichier CSV (les clés du dictionnaire JSON)
        csv_writer.writerow(data[0].keys())
        
        # Écrire les données dans le fichier CSV
        for item in data:
            csv_writer.writerow(item.values())
    print(f"Données enregistrées au format CSV dans le fichier : {filename}")

# Point d'entrée du script
if __name__ == "__main__":
    # Récupérer les données depuis l'API
    api_data = fetch_data(api_url)
    
    # Vérifier si les données ont été récupérées avec succès
    if api_data:
        # Enregistrer les données au format JSON
        save_as_json(api_data, "data.json")
        
        # Enregistrer les données au format CSV
        save_as_csv(api_data, "data.csv")
