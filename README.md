# vscode-gcp

## How to authenticate to gcloud

https://googleapis.dev/python/google-api-core/latest/auth.html

## Troubleshoot warning about quota's

1. gcloud auth login
2. gcloud config set project YOUR_PROJECT_ID
3. gcloud auth application-default set-quota-project YOUR_PROJECT_ID

NOTE: if you want to revoke this later
```gcloud auth application-default revoke```