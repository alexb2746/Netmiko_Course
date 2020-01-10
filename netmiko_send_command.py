import os
from getpass import getpass
from netmiko import ConnectHandler

log_file = open("log.txt", "w")

device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command("Show version")
log_file.write(output)
net_connect.disconnect()
