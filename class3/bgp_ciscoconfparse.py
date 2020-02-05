import os
from ciscoconfparse import CiscoConfParse
from getpass import getpass
from netmiko import ConnectHandler

bgp_peers = []
bgp_config = ""

with open("bgp_config.txt") as bgp_file:
    bgp_config = CiscoConfParse(bgp_file)

bgp = bgp_config.find_objects(r"^router bgp")

for child in bgp[0].children:
    if "neighbor" in child.text:
        neighbor_ip = child.text[10:-1]
        for setting in child.children:
            if "remote-as" in setting.text:
                remote_as = setting.text[12:-1]
                neighbor = (neighbor_ip, remote_as)
                bgp_peers.append(neighbor)

print(bgp_peers)

