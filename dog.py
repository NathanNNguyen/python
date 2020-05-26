import requests

api_url = "http://shibe.online/api/shibes?count=1"

params = {"count": 10}
res = requests.get(api_url, params=params)

status_code = res.status_code
print("status code:", status_code)

res_json = res.json()

print(res_json)
