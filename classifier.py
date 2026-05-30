import requests
from prompt_templates import FEEDBACK_PROMPT_TEMPLATE

# Simulated access (in real deployment, store these in .env or IBM Cloud secrets manager)
WATSONX_API_KEY = "jb34jb324h35324j34h53g3h45j2jg5h34hj532jh4j5h4"
WATSONX_PROJECT_ID = "ik234233"
WATSONX_MODEL_ID = "google/flan-t5-xl" 
WATSONX_API_URL = "https://us-south.ml.cloud.ibm.com/v1/watsonx/generate"

def classify_feedback(feedback_text: str) -> str:
    prompt = FEEDBACK_PROMPT_TEMPLATE.format(feedback=feedback_text.strip())

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {WATSONX_API_KEY}"
    }

    payload = {
        "model_id": WATSONX_MODEL_ID,
        "project_id": WATSONX_PROJECT_ID,
        "inputs": [
            {
                "input": prompt,
                "parameters": {
                    "decoding_method": "greedy",
                    "max_new_tokens": 10
                }
            }
        ]
    }

    response = requests.post(WATSONX_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()

    return result["results"][0]["generated_text"].strip()
