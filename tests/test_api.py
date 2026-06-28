import requests

url = "http://127.0.0.1:8000/ask"

question = {"question": "What is the academic calendar?"}

response = requests.post(url, json=question)

print(response.json())