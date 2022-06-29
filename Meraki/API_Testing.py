import requests
import json
import pprint

url = "https://api.meraki.com/api/v1/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.get(url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['name'] == 'DevNet Test Org':
        orgId = response_org['id']

print(orgId)