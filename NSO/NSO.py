import requests
import json
from pprint import pprint

# Dont forget sudo ufw allow 8080
url_base = 'https://sandbox-nso-1.cisco.com:443/restconf'
auth = ("developer", "Services4Ever")

# Other useful headers

#    'application/vnd.yang.api+json',
#    'application/vnd.yang.datastore+json',
#    'application/vnd.yang.data+json',

headers = {'Accept': 'application/vnd.yang.collection+json'}

# Get request to NSO
response = requests.get(f'{url_base}/data/tailf-ncs:devices/device=core-rtr01', auth=auth, headers=headers, verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))
# print(response)

# Parse out devices from response body
devices = response['tailf-ncs:device']
# print(json.dumps(devices, indent=2, sort_keys=True))
# print(devices[0]['name'])

print(f"Name: {devices[0]['name']}")
print(f"IP: {devices[0]['address']}")
print(f"Auth Group: {devices[0]['authgroup']}")
print(" ")

# for device in devices:
    # print(f"Name: {device['name']}")
    # print(f"IP: {device['address']}")
    # print(f"SSH Port: {device['port']}")
    # print(f"Auth Group: {device['authgroup']}")
    # print(device)
    # print(" ")