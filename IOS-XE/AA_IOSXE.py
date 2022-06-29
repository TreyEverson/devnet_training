import requests
import json

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces-state/"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

response = response['ietf-interfaces:interfaces-state']['interface']
# print(response[0].keys())

device_info = {}

for key in response[0].keys():
    # print(response[0][key])
    # print('-' * 50)

    name = key
    device_info[name] = response[0][key]

for key in device_info.keys():
    print(key, ':', device_info[key])
    print('-' * 10)

if device_info['oper-status'] == 'up':
    print('--- STATUS IS OPERATIONAL ---')
