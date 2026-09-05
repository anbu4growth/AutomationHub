#!/bin/bash

set -e

PROJECT_ID="automation-hub-502406"
REGION="asia-south1"
JOB_NAME="automation-hub"

echo "========================================="
echo "AutomationHub Deployment"
echo "========================================="

echo "Building Docker Image..."
docker build -t gcr.io/$PROJECT_ID/$JOB_NAME:latest .

echo "Configuring Docker..."
gcloud auth configure-docker --quiet

echo "Pushing Docker Image..."
docker push gcr.io/$PROJECT_ID/$JOB_NAME:latest

echo "Deploying Cloud Run Job..."

gcloud run jobs create $JOB_NAME \
    --image=gcr.io/$PROJECT_ID/$JOB_NAME:latest \
    --region=$REGION \
    --max-retries=1 \
    --task-timeout=900 \
    --set-env-vars=HEADLESS=true \
    --set-env-vars=GOOGLE_SHEET_ID=$GOOGLE_SHEET_ID \
    --update-secrets=TF_USERNAME=tf-username:latest \
    --update-secrets=TF_PASSWORD=tf-password:latest \
    --update-secrets=GOOGLE_CREDENTIALS=google-service-account:latest

echo ""
echo "Deployment Completed Successfully."