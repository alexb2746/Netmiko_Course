import os
from getpass import getpass
from netmiko import ConnectHandler

log_file = open("log.txt", "w")

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_session.txt",
    "fast_cli": True    
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command("ping google.com")
print(output)

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

output = net_connect.send_config_set(cfg)
print(output)

output = net_connect.send_command("ping google.com")
print(output)
net_connect.disconnect()
