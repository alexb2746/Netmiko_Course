import os
from getpass import getpass
from netmiko import ConnectHandler

devices = ['nxos1.lasthop.io', 'nxos2.lasthop.io']

for device in devices:

    device1 = {
        "host": device,
        "username": "pyclass",
        "password": "88newclass",
        "device_type": "cisco_nxos",
        "session_log": "my_session.txt",
    }

    net_connect = ConnectHandler(**device1)

    output = net_connect.send_config_from_file('my_changes.txt')
    print(output)

    save = net_connect.save_config()
    print(save)

    net_connect.disconnect()
