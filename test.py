import requests

BASE = 'http://127.0.0.1:5000/1'

response = requests.put(BASE , {'name': 'kira', 'likes': 10, 'views': 100})
print(response.json())
