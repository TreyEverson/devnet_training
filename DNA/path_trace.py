from email.charset import BASE64
from urllib import response
import requests
import json
from pprint import pprint

BASE_URL = "https://sandboxdnac2.cisco.com"

USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'

# Authorization - Requesting Token
AUTH_URI = '/dna/system/api/v1/auth/token'
response = requests.post(BASE_URL + AUTH_URI, auth=(USERNAME, PASSWORD), verify=False).json()

# print(response['Token'])
token = response['Token']

# Get Source Device IP

headers = {
    'X-Auth-Token': token,
    'User-Agent': "PostmanRuntime/7.16.3",
    'Content-Type': 'application/json'
}

'''
headers = {
    'x-auth-token': token,
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "393a9fdd-f109-4fd3-821b-0ae2a03da256,3d2299b4-7515-4f80-9964-b33c2ae9c2ab",
    'Host': "sandboxdnac2.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
'''

DEVICE_URI = '/dna/intent/api/v1/network-device'

queryParams = {}

response = requests.get(BASE_URL + DEVICE_URI, headers=headers, verify=False).json()
# pprint(response['response'][0])
source_device = {'hostname': response['response'][0]['hostname'], 'ip': response['response'][0]['managementIpAddress']}
dest_device = {'hostname': response['response'][1]['hostname'], 'ip': response['response'][1]['managementIpAddress']}
pprint(source_device)
pprint(dest_device)