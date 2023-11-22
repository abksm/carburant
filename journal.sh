# venv
python3 -m venv venv
source venv/bin/activate

pip install psycopg2-binary
pip install "apache-airflow[celery]==2.7.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.10.txt"







# === Airflow local ===========================================================================================
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow db init
airflow users create --username admin --firstname Yohann --lastname Zapart --role Admin --email yohann@zapart.com

# starting scheduler
source venv/bin/activate
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow scheduler

# starting webserver
source venv/bin/activate
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow webserver --port 8080




# === postgresql ===============================================================================================
sudo apt install postgresql

sudo -i -u postgres psql <<EOF
CREATE DATABASE carburants;
CREATE USER yzpt WITH PASSWORD 'yzpt';
ALTER ROLE yzpt SET client_encoding TO 'utf8';
ALTER ROLE yzpt SET default_transaction_isolation TO 'read committed';
ALTER ROLE yzpt SET timezone TO 'Europe/Paris';
GRANT ALL PRIVILEGES ON DATABASE carburants TO yzpt;
EOF


sudo -i -u yzpt psql carburants <<EOF
DROP TABLE IF EXISTS raw_fields;
EOF

sudo -i -u yzpt psql carburants <<EOF
CREATE TABLE IF NOT EXISTS records (
    record_timestamp TIMESTAMP,
    id BIGINT,
    latitude REAL,
    longitude REAL,
    cp VARCHAR(50),
    pop TEXT,
    adresse TEXT,
    ville VARCHAR(50),
    horaires TEXT,
    services TEXT,
    gazole_maj TIMESTAMP,
    gazole_prix REAL,
    sp95_maj TIMESTAMP,
    sp95_prix REAL,
    e85_maj TIMESTAMP,
    e85_prix REAL,
    gplc_maj TIMESTAMP,
    gplc_prix REAL,
    e10_maj TIMESTAMP,
    e10_prix REAL,
    sp98_maj TIMESTAMP,
    sp98_prix REAL,
    carburants_disponibles VARCHAR(50),
    carburants_indisponibles VARCHAR(50),
    horaires_automate_24_24 TEXT,
    departement VARCHAR(50),
    code_departement VARCHAR(50),
    region VARCHAR(50),
    code_region VARCHAR(50),
    PRIMARY KEY (record_timestamp, id)
);
EOF



SELECT id, record_timestamp from records ORDER BY record_timestamp DESC LIMIT 5;

sudo -i -u yzpt psql carburants <<EOF > query_results.txt
SELECT * FROM raw_fields ORDER BY record_timestamp DESC;
EOF

sudo -i -u yzpt psql carburants
SELECT id, record_timestamp, ville, adresse, latitude, longitude FROM records ORDER BY record_timestamp DESC LIMIT 5;


# === DOCKER ===================================================================================================

# === Airflow Docker ===========================================================================================
# https://airflow.apache.org/docs/docker-stack/index.html
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
docker compose up airflow-init
docker compose down --volumes --remove-orphans
docker compose up


git add . && git commit -m "airflow docker" && git push origin docker   