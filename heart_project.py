import requests
import json

# --- Replace these with your actual credentials ---
API_KEY = "B_uTRrsl5vX14ZvVxR7KJE_JfyAk4erD3ED37GZYRnsD"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/8ae9e318-0ba5-4b59-b575-caca7d798513/predictions?version=2021-05-01"


# --- Get IAM access token ---
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'},
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
)
ml_token = token_response.json()["access_token"]

# --- Set headers for the request ---
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {ml_token}'
}

# --- Example input for heart disease prediction ---
payload = {
    "input_data": [{
        "fields": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope",
            "ca", "thal"
        ],
        "values": [[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]
        # Note: this is an example row from UCI dataset
    }]
}

# --- Make the POST request to AutoAI scoring endpoint ---
response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)

# --- Show the prediction result ---
prediction = response.json()
print("Prediction:", json.dumps(prediction, indent=2))
