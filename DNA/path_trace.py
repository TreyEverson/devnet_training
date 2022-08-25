from email.charset import BASE64
from http.client import ResponseNotReady
from importlib.resources import path
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

# Get Source/Destination Device IP

headers = {
    'X-Auth-Token': token,
    'User-Agent': "PostmanRuntime/7.16.3",
    'Content-Type': 'application/json'
}

DEVICE_URI = '/dna/intent/api/v1/network-device'

response = requests.get(BASE_URL + DEVICE_URI, headers=headers, verify=False).json()
# pprint(response['response'][0])
source_device = {'hostname': response['response'][0]['hostname'], 'ip': response['response'][0]['managementIpAddress']}
dest_device = {'hostname': response['response'][1]['hostname'], 'ip': response['response'][1]['managementIpAddress']}
pprint(source_device)
pprint(dest_device)

# Create Path Trace

PATH_TRACE_URI = '/dna/intent/api/v1/flow-analysis'

path_trace_payload = {
    'sourceIP': source_device['ip'],
    'destIP': dest_device['ip'],
    'inclusions': [
        'INTERFACE-STATS',
        'DEVICE-STATS',
        'ACL-TRACE',
        'QOS-STATS'
        ],
    'protocol': 'icmp'
}

response = requests.post(f"{BASE_URL}{PATH_TRACE_URI}", headers=headers, json=path_trace_payload, verify=False).json()
# pprint(response['response'])
flow_analysis_id = response['response']['flowAnalysisId']
pprint(flow_analysis_id)

# Get Path Trace Result

response = requests.get(f"{BASE_URL}{PATH_TRACE_URI}/{flow_analysis_id}", headers=headers, verify=False).json()
pprint(response['response'])

# Get Path Traces
response = requests.get(f"{BASE_URL}{PATH_TRACE_URI}", headers=headers, verify=False).json()
pprint(response['response'])

# Delete Path Trace
response = requests.delete(f'{BASE_URL}{PATH_TRACE_URI}/{flow_analysis_id}', headers=headers, verify=False)
print(response.status_code)