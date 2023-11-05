# Open Data & GCP : Prix des carburants en France

### Sources de données

Wesh bin wlh le jeu de données des carburants il est cool y'a moyen de faire un beau travail dessus.

[https://data.economie.gouv.fr/explore/dataset/prix-des-carburants-en-france-flux-instantane-v2/information/](https://data.economie.gouv.fr/explore/dataset/prix-des-carburants-en-france-flux-instantane-v2/information/)

Ils disent qu'il est mis à jour toutes les 10 minutes c'est parfait.

Dans l'onglet 'API', tout en bas il y a l'adresse de la requete, en réglant limit=null et timezone=Europe/Paris ça donne ça :

https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?timezone=Europe%2FParis

attention ça renvoi 10 000 lignes, pour t'entrainer tu peux mettre limit=3 par exemple, ça te renverra que 3 lignees, comme ça :

[https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?limit=3&timezone=Europe%2FParis](https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?limit=3&timezone=Europe%2FParis)

J'te conseille :

  - faire un script python qui récupère les données avec le module 'requests', sauvegarder les données dans des fichiers .csv et .json en local. 
  
  Pour l'instant ne t'emmerde pas à tout récolter c'est pas l'important, copilot se chargera plus tard t'écrire toutes les colonnes etc, comme ça je dirais simplement de récolter : 

    - id
    - adresse
    - ville
    - latitude
    - longitude
    - prix SP98
    - maj SP98
    - prix Gazole
    - maj Gazole
    - prix GPL
    - maj GPL