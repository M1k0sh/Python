import json

with open('sample-data.json', "r") as json_file:
    a = json.load(json_file)
    d = dict(a)

#check
print(d['totalCount'])
print(d['imdata'])