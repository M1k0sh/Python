import json

with open('sample-data.json', "r") as json_file:
    a = json.load(json_file)

print('Interface Status')
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

imdata = a["imdata"]

for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]:
            if ("33" in imdata[i][j][k]["dn"]) or ("34" in imdata[i][j][k]["dn"]) or ("35" in imdata[i][j][k]["dn"]):
                print(f'{imdata[i][j][k]["dn"]}                              {imdata[i][j][k]["speed"]}   {imdata[i][j][k]["mtu"]}') 
