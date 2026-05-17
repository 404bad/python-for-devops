# YAML file handling
# super imprtant in devops
# used in kubernetes, ansible, docker compose, github actions

# install PyYAML : pip install pyyaml

import yaml

with open("config.yml","r") as file:
    data = yaml.safe_load(file)
print(data)
