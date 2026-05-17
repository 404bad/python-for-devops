# check server status

import os

def check_server():
    response = os.system("ping -c 1 google.com")
    #print(response)

    if response == 0:
        return "server reachable"

    return "Server unreachable"

status = check_server()

print(status)

 # function with subprocess

import subprocess

def run_commands(command):
    result = subprocess.run(
        command,
        shell= True,
        text=True,
        capture_output=True
    )

    return result.stdout

output = run_commands("kubectl get pods")

print(output)
