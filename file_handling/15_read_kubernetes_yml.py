import yaml

with open("deployment.yml", "r") as file:

    data = yaml.safe_load(file)

print(data["kind"])
