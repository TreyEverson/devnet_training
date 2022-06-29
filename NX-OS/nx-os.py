from distutils.log import warn
import requests
import json
from pprint import pprint

def getToken():
    url = "https://sandbox-nxos-1.cisco.com/api/aaaLogin.json"

    payload = "{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\":\"admin\",\n            \"pwd\":\"Admin_1234!\"\n        }\n    }\n}"
    headers = {
    'Content-Type': 'application/json-rpc',
    'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
    }

    response = requests.post(url, headers=headers, data=payload, verify=False).json()

    # pprint(response)

    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    # pprint(token)

    cookies = {}

    # --- IMPORTANT ---
    cookies['APIC-cookie'] = token
    # --- IMPORTANT ---

    return cookies

def createVLAN(cookies):
    url = "https://sandbox-nxos-1.cisco.com:443/api/mo/sys/bd.json"

    payload = json.dumps({
    "bdEntity": {
        "children": [
        {
            "l2BD": {
            "attributes": {
                "fabEncap": "vlan-200",
                "pcTag": "1"
            }
            }
        }
        ]
    }
    })
    headers = {
    'Accept': 'application/json-rpc',
    'Content-Type': 'application/json-rpc'
    }

    post_response = requests.post(url, headers=headers, data=payload,cookies=cookies, verify=False).json()

    pprint(post_response)

def getVLAN(cookies):
    url = "https://sandbox-nxos-1.cisco.com:443/api/mo/sys/bd/bd-vlan-200.json"

    payload={}
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }

    get_response = requests.get(url, headers=headers, data=payload, cookies=cookies, verify=False).json()

    # pprint(get_response)

cookies = getToken()
create = createVLAN(cookies)
get = getVLAN(cookies)

print(create, '\n---\n', get)