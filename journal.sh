git checkout -b yzpt
git add .
git commit -m "add journal.sh"
git push origin yzpt

git checkout main
git config pull.rebase false
git pull origin main

git branch -d yzpt
git push origin --delete yzpt

git remote show origin

pip freeze > requirements.txt

# venv
python3 -m venv venv
source venv/bin/activate

pip install requests
pip install "apache-airflow[celery]==2.7.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.10.txt"
pip install google-cloud-storage
pip install google-cloud-bigquery

# gcloud config
PROJECT_ID=carburants-yzpt

gcloud projects create $PROJECT_ID --name="Carburants"
gcloud config set project $PROJECT_ID

gcloud iam service-accounts create $PROJECT_ID-SA --display-name="$PROJECT_ID Service Account"
SERVICE_ACCOUNT_EMAIL=$PROJECT_ID-SA@$PROJECT_ID.iam.gserviceaccount.com
gcloud iam service-accounts keys create key-$PROJECT_ID-SA.json --iam-account=$SERVICE_ACCOUNT_EMAIL

# enable APIs
gcloud services enable bigquery.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable composer.googleapis.com

# permissions
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" --role="roles/bigquery.dataEditor"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" --role="roles/storage.admin"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" --role="roles/composer.admin"


# service accounts list
gcloud iam service-accounts list

BILLING_ACCOUNT_ID=$(gcloud alpha billing accounts list --format="value(ACCOUNT_ID)")
gcloud billing projects link $PROJECT_ID --billing-account=$BILLING_ACCOUNT_ID


# composer







# Airflow Docker :
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
docker compose up airflow-init
