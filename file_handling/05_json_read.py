# json file handling is very important in DevOps
# used in APIS, Kubernetes, Terraform uotputs, cloud tools

import json

with open("cofig.json", "r") as file:
    data = json.load(file)

print(data["name"])

for key,value in data.items():
    print(key, ":", value)

    
