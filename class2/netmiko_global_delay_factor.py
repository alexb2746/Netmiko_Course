import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

start_time = datetime.now()

log_file = open("log.txt", "w")

device1 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
    "session_log": "my_session.txt"
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command("Show lldp neighbors detail")
print(output)
log_file.write(output)
net_connect.disconnect()
end_time = datetime.now() 

print(end_time - start_time)
