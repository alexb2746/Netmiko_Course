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

output = net_connect.send_command("ping", expect_string="Protocol")
print(output)
output += net_connect.send_command("\n", expect_string="address")
print(output)
output += net_connect.send_command("8.8.8.8", expect_string="count")
print(output)
output += net_connect.send_command("\n", expect_string="size")
print(output)
output += net_connect.send_command("\n", expect_string="seconds")
print(output)
output += net_connect.send_command("\n", expect_string="commands")
print(output)
output += net_connect.send_command("\n", expect_string="sizes")
print(output)
output += net_connect.send_command("\n", expect_string="!!")

print(output)
net_connect.disconnect()
