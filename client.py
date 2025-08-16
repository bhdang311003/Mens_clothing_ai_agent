import requests

url = "http://127.0.0.1:8000/ask"

query = "What is the most popular product?"

payload = {"query": query}
response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:", response.json())
