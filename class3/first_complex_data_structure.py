import yaml

complex_data = [{"mac_addr": "0062.ec29.70fe", "ip_addr": "10.220.88.1", "interface": "Gi0/0/0"}, 
    {"mac_addr": "c89c.1dea.0eb6", "ip_addr": "10.220.88.20", "interface": "Gi0/0/0"}, 
    {"mac_addr": "a093.5141.b780", "ip_addr": "10.220.88.22", "interface": "Gi0/0/0"}, 
    {"mac_addr": "0001.00ff.0001", "ip_addr": "10.220.88.37", "interface": "Gi0/0/0"},
    {"mac_addr": "0002.00ff.0001", "ip_addr": "10.220.88.38", "interface": "Gi0/0/0"}
]

for data in complex_data:
    print(data)


devices = [{"device_name": "cisco3", "host": "cisco3.lasthop.io", "username": "pyclass", "password": "88newclass"},
    {"device_name": "cisco4", "host": "cisco4.lasthop.io", "username": "pyclass", "password": "88newclass"},
    {"device_name": "arista1", "host": "arista1.lasthop.io", "username": "pyclass", "password": "88newclass"},
    {"device_name": "arista2", "host": "arista2.lasthop.io", "username": "pyclass", "password": "88newclass"},
    {"device_name": "nxos1", "host": "nxos1.lasthop.io", "username": "pyclass", "password": "88newclass"},
    {"device_name": "nxos2", "host": "nxos2.lasthop.io", "username": "pyclass", "password": "88newclass"}
]

for device in devices:
	print(device)



filename = "outfile.yml"
with open(filename, "wt") as f:
    yaml.dump(devices, f, default_flow_style=False)
