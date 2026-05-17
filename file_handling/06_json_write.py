# write json

import json

data = {
    "server": "web1",
    "status": "running"
}

with open ("server.json", "w") as file:
    json.dump(data,file,indent=4)
