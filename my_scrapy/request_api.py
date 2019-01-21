import requests


response=requests.get('https://api.github.com')
print(response.url)
print(response.status_code)
print(response.reason)
print(response.headers)
print(response.request.headers)
print(response.content)
print(response.json()['team_url'])
print(response.history)

response=requests.get('http://api.github.com')
print(response.url)
print(response.history)
