from email.mime import base
from urllib import response
import requests
import json
from pprint import pprint

# Authenticating to DNAC using Python
base_url = "https://sandboxdnac.cisco.com/"
auth_endpoint = 'api/system/v1/auth/token'
user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(base_url + auth_endpoint, auth=(user, pw), verify=False).json()
# print(response)
token = response['Token']
# print(token)

########## Can now make API calls with token ##########

# Get client health status

client_health_endpoint = 'dna/intent/api/v1/client-health'

headers = {
    'x-auth-token' : token
}

response = requests.get(base_url + client_health_endpoint, headers=headers, verify=False).json()
pprint(response)

print(
    f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")


scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")