import subprocess

try:
    result = subprocess.run(
        ["df","-h"],
        check=True,
        text=True,
        capture_output=True
    )

    print(result.stdout)
except subprocess.CalledProcessError:
    print("Disk Command failed")

