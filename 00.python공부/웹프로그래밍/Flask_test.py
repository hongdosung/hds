import requests, json

BASE = "http://127.0.0.1:5000/"
# Set request's header.
headers = {"Content-Type": "application/json; charset=utf-8"}
# Set data.
data = {"name": "John", "age": 30}
# 
response = requests.post(BASE + 'user/1', headers=headers, json=data)

print("Status Code: ", response.status_code)
print("JSON Response: ", response.json())
