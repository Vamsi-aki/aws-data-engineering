import pandas as pd
import requests

# TODO: Paste your API Gateway endpoint here (must include /stage/resource)
URL = "https://your-api-id.execute-api.region.amazonaws.com/STAGE/RESOURCE"

# Load test data
data = pd.read_csv('data/TestSample.csv', sep=',')

# Iterate over each row and send it to the API
for i in data.index:
    try:
        payload = data.loc[i].to_json()
        response = requests.post(URL, data=payload)

        print(payload)
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Error on row {i}:", e)
        print(data.loc[i])
