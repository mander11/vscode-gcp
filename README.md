# vscode-gcp

Proof of concept repo, that demonstrates:

1. vscode - from docker image
2. google genai example usage
3. google cloud storage example usage

## Pre-requisites

### 1. Create config.py

Copy `config_COPY_ME.py` => `config.py`

Replace values appropriately

NOTE: you can retreive genai token by visiting https://aistudio.google.com/app/apikey

### 2. Authenticate to gcloud

https://googleapis.dev/python/google-api-core/latest/auth.html

1. `gcloud auth application-default login`
2. `gcloud config set project <YOUR_PROJECT_ID>`
3. `gcloud auth application-default set-quota-project <YOUR_PROJECT_ID>`

## How to Run

```python main.py```