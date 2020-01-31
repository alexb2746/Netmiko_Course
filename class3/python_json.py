import json
from pprint import pprint

filename = "my_json_file.json"
with open(filename) as file:
    data = json.load(file)

ipv4 = []
ipv6 = []

for key in data.keys():
    if 'ipv4' in data[key]:
        ipv4.append(data[key]['ipv4'])

    if 'ipv6' in data[key]:
        ipv6.append(data[key]['ipv6'])

print(ipv4)
print('\n', ipv6)
