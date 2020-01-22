import os
from netmiko import ConnectHandler

log_file = open("log.txt", "w")

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command_timing("ping")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("8.8.8.8")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")

print(output)
net_connect.disconnect()
