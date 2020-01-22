import os
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

commands = ["show version", "show lldp neighbors"]

for command in commands:
    output = net_connect.send_command(command, use_textfsm=True)
    print(output)

    if command == "show lldp neighbors":
        print("ciscoios4 is connected to the HPE switch interface: ")
        print(output[0]['neighbor_interface'])
net_connect.disconnect()
