from operator import imod
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

# --- AUTH ---
token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
meraki = MerakiSdkClient(token)

# --- GET ORGS ---
orgs = meraki.organizations.get_organizations()
# pprint(orgs)

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

# print(orgId)

params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)
# pprint(networks)

for network in networks:
    if network['name'] == 'DNSMB1':
        netId = network['id']

vlans = meraki.vlans.vlans_controller.get_network_vlans(netId)
pprint(vlans)

