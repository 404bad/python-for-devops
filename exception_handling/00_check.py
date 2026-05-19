import subprocess

try:
    subprocess.run(
        ["ls","/random-folder"],
        check=True
    )

except subprocess.CalledProcessError as e:
    print("Command failed, ", e)

# check=True means if command fails raise exception
