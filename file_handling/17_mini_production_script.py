# Mini Production Script

import json
from datetime import datetime

def log_deployment(service):

    log = {
        "service": service,
        "time": str(datetime.now())
    }

    with open("deployments.json", "a") as file:

        file.write(json.dumps(log))
        file.write("\n")


input_service = input("Enter the name of service: ")
log_deployment(input_service)

