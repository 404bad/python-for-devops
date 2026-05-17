import yaml

data = {
    "app": "nginx",
    "replicas": 3
}

with open("output.yaml", "w") as file:

    yaml.dump(data, file)
