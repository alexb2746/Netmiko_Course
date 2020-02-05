import os
from ciscoconfparse import CiscoConfParse
from getpass import getpass
from netmiko import ConnectHandler

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command("Show run")

cisco4_config = CiscoConfParse(output.splitlines())

interfaces = cisco4_config.find_objects(r"^interface")

for interface in interfaces: 
    for child in interface.children: 
        if child.text.startswith(" ip address"):
            print(interface.text) 
            print(child.text) 

net_connect.disconnect()
