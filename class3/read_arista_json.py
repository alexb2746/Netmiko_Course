import json
from pprint import pprint

filename = "arista_data.json"
with open(filename) as file:
    data = json.load(file)

my_data = {}

for neighbor in data['ipV4Neighbors']:
    my_data[neighbor['address']] = neighbor['hwAddress']

print(my_data)
