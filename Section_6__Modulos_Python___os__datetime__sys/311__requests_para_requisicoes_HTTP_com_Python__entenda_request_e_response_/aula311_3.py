# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests


# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response)
print(response.status_code)
print(response.headers)
