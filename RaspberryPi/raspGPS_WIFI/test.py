import requests
import json


URL = 'http://34.64.124.225/test'
data = {"petId":"123"}
headers = {'Content-Type' : 'application/json'}
res = requests.post(URL, headers=headers, data=json.dumps(data))

print(res.status_code)
#print(res.text)
print(res.json())
