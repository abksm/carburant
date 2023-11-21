# venv
python3 -m venv venv
source venv/bin/activate

pip install requests
pip install google-cloud-storage
pip install google-cloud-bigquery
pip freeze > requirements.txt



# =====================   AIRFLOW   ============================================================================
# https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=2142s

# === Airflow Docker ===========================================================================================
# https://airflow.apache.org/docs/docker-stack/index.html
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
docker compose up airflow-init
docker compose down --volumes --remove-orphans
docker compose up


# === Airflow py_env ===========================================================================================
pip install "apache-airflow[celery]==2.7.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.10.txt"
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow db init
airflow users create --username admin --firstname Yohann --lastname Zapart --role Admin --email yohann@zapart.com

# webserver starter
source venv/bin/activate
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow webserver --port 8080
sudo kill 4426

# sheduler starter
source venv/bin/activate
export AIRFLOW_HOME=/home/yzpt/projects/carburant_gcp
airflow scheduler

# request dag ok


# === postgresql ===============================================================================================
# https://doc.ubuntu-fr.org/postgresql
sudo apt install postgresql


sudo -i -u postgres psql <<EOF
CREATE DATABASE carburants;
CREATE USER yzpt WITH PASSWORD 'yzpt';
ALTER ROLE yzpt SET client_encoding TO 'utf8';
ALTER ROLE yzpt SET default_transaction_isolation TO 'read committed';
ALTER ROLE yzpt SET timezone TO 'Europe/Paris';
GRANT ALL PRIVILEGES ON DATABASE carburants TO yzpt;
EOF

sudo -i -u yzpt psql carburants

# drop table
DROP TABLE IF EXISTS raw_fields;

CREATE TABLE IF NOT EXISTS raw_fields (
    record_timestamp TIMESTAMP,
    id BIGINT,
    latitude TEXT,
    longitude REAL,
    cp TEXT,
    pop TEXT,
    adresse TEXT,
    ville TEXT,
    horaires TEXT,
    services TEXT,
    prix TEXT,
    lon REAL,
    lat REAL,
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
    carburants_disponibles TEXT,
    carburants_indisponibles TEXT,
    horaires_automate_24_24 TEXT,
    services_service TEXT,
    departement TEXT,
    code_departement TEXT,
    region TEXT,
    code_region TEXT,
    PRIMARY KEY (record_timestamp, id)
);

# psql get columns of a table
\d raw_fields

# select *...
SELECT id, record_timestamp FROM raw_fields LIMIT 10;

SELECT id, lat, lon FROM raw_fields LIMIT 10;


pip install psycopg2-binary

# local pipeline ok


# rename branch
git branch -m yzpt local