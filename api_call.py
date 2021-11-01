import requests

url = "http://127.0.0.1:8000/my_app/my_app/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

new= response.text
print(new)