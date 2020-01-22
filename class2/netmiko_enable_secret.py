import os
from netmiko import ConnectHandler
import time

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "secret": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)

output = net_connect.find_prompt()
print(output)

output = net_connect.config_mode()      
print(output)

output = net_connect.find_prompt()      
print(output)

output = net_connect.exit_config_mode()      
print(output)

output = net_connect.find_prompt()      
print(output)

output = net_connect.write_channel('disable \n')      
print(output)

time.sleep(2)

output = net_connect.read_channel()      
print(output)

output = net_connect.enable()      
print(output)

output = net_connect.find_prompt()      
print(output)

net_connect.disconnect()
