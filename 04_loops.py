# A for loop in python is heavily used in DevOps for automation, scripting, server, management, deployments, monitoring, and cloud tasks.

# Basic for loop

for item in range(5):
    print(item)

for item in range(5):
    if item == 3:
        continue
    print(item)


#example
servers = ["web1","web2","web3"]

for server in servers:
    print(server)

# Common DevOps Uses

## 1. LOOP through servers

servers = ["192.168.1.10","192.168.1.11","192.168.1.12"]

for server in servers:
    print(f"Conecting to {server}")


# this is used in ssh automation, ansible scripts, health cheks

## 2. loop through files
import os

for file in os.listdir("/var/log"):
    print(file)

# this is used for log analysis, cleanup scripts, backup automation

## 3. Run Command multiple times

commands = ["docker ps","kubectl get pods", "df -h"]

for cmd in commands:
    print(f"Running: {cmd}")

for cmd in commands:
    os.system(cmd)


## Using range()

for i in range(4):
    print(i)

# for 0 to 4 but 4 is excluded. so output is 0,1,2,3

## loop with start and end
for i in range(1,6):
    print(i)

# start is alwauys considered but the end is neglegted

## loop with step
for i in range(0,10,2):
    print(i)

# the 2 is steps so it print from 0 to 10 like this 0, 0+2, 2+2, 4+2,6+2 
# 0-10 . 10 is already excluded . so it only goes upto 8

## break ans contibue

# break stops the loop
for i in range(10):
    if i == 6:
        break
    print(i)

# contibue skips current iteration
for i in range(10):
    if i == 2:
        continue
    print(i)




## Nested Loop
servers = ["web1","web2"]
ports = ["80","443"]

for server in servers:
    for port in ports:
        print(server, port)

# A for loop is used to iterate over items like lists, files, servers, pods or commands, In DevOps we use it for automation tasks such as deployments, monitoring, backups, and infrastructure scripting.


