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