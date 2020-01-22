import os
from getpass import getpass
from netmiko import ConnectHandler

hosts = ['nxos1.lasthop.io', 'nxos2.lasthop.io']
host_password = getpass()

for host in hosts:
    print(host)
    net_connect = ConnectHandler(
        host="nxos1.lasthop.io",
        username="pyclass",
        password=host_password,
        device_type="cisco_nxos",
        session_log="my_session.txt",
    )

    print(net_connect.find_prompt())
    net_connect.disconnect()
