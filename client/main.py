import requests

url = 'http://localhost:3000/users'  # Ensure the route is correct
headers = {'Content-Type': 'application/json'}
inp_text = 'chatle'
data = {'data': inp_text}

response = requests.post(url, json=data, headers=headers)
print(response.text)
