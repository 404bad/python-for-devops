#example with json
# very commoon in APIs confgis

import json

try:
    with open("config.json") as file:
        data = json.load(file)

    print(data)

except FileNotFoundError:
    print("Config file missing")
except json.JSONDecodeError:
    print("Invalid json")
