import os
from getpass import getpass
from netmiko import ConnectHandler
import yaml

with open("/home/boley/.netmiko.yml") as yml_file:
    yaml_out = yaml.load(yml_file)

devices = yaml_out

log_file = open("log.txt", "w")

device1 = {
    "host": devices['cisco3']['host'],
    "username": "pyclass",
    "password": "88newclass",
    "device_type": devices['cisco3']['device_type'],
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command("Show version")
print(output)
net_connect.disconnect()
