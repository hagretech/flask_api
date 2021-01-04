import requests

BASE = 'http://127.0.0.1:5000/video/3'

response = requests.get(BASE , {'name':'kira2', 'likes': 176870, 'views': 145000})
print(response.json())
