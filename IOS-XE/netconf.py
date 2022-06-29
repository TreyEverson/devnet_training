from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
from router_info import router
from lxml import etree

file_netconf_filter = open('/Users/treverso/Documents/DevNet/devnet_training/IOS-XE/netconf-filter.xml').read()

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>GigabitEthernet2</name>
    </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces-state>
</filter>
"""

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces-state>
</filter>
"""

hostname_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm"/>
</filter>
'''

# rpc_elem = etree.fromstring(netconf_filter)

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    
    print('Connected')
    interface_netconf = m.get(file_netconf_filter)
    print(interface_netconf)
    print('Getting running config')

'''
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="  "))
print('*' * 25 + 'Break' + '*' * 50)
# XMLTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"Pakcets In {op_state['statistics']['in-unicast-pkts']}")
'''