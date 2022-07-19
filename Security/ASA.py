import requests
import json

url = "https://{IP_ADDR}/api/routing/static"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Tuple for authentication (uname, pass)
userpw = ('cisco', 'cisco')

get_response = requests.get(
    url, headers=headers, auth=userpw, verify=False).json()['items']

print(json.dumps(get_response, indent=2, sort_keys=True))