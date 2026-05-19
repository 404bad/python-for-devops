# practical DevOps script example

# Check if a service is active

import subprocess

service = input("Enter the name of teh service: ")

try:
    result = subprocess.run(
        ["systemctl","is-active", service],
        check=True,
        text=True,
        capture_output=True
    )


    print(f"{service} is running")

except subprocess.CalledProcessError:
    print(f"{service} is not running")
