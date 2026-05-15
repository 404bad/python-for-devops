# What is python?

Python is a high level programming language created to make coding somple, readable, and powerful. It is widely used in areas like:

- Web application
- Automation and scripting
- Data science
- Artificaila Intelligence
- Cybersec
- DevOps and Cloud Engineering

Python is beginner-friendlt because its syntax looks close to normal english.

```py
print("Hello DevOps")

```

this single line prints text on the screen.

# What is scripting?

A script is a small program written to automate tasks.

Instead of manually repeating commands again and again, you write ascripy once and let the computer do the work automatically.

Example tasks we can automate with scripts:

- creating file and folders
- Backing up servers
- Deploying applications
- Monitoring CPU/RAM usage
- Mnaging Docker containers
- Running Linux commands automatically
- Parsing logs
- Sending alerts

so : Scripting =  Automating repetitive tasks using code.

# Why Python is used for scripting in DevOps?

In DevOps, engineers constantly scutomate infrastructure, deployments, monitoring and server management.

Python became one of the most popular DevOps scripting languages becuase it is:

1. Easy to read and write
2. Excellent for Automation
3. Huge Library


### Python in DevOps work

1. Infrastructure Automation
2. CI/CD pipeines
3. Monitoring and Alerts
4. Docker and kubernetes Automation


## Difference between Programming anD scripting
programming: builds full application, larger systems, can be complex, exmple: webapp
Scripting: Automates tasks, Smaller Automation, USually short/simple, exmple: Backup Script

## E	xample of a simple DevOps Python script

this script check disk usage

```py
	import shutil

	total, used, free = shutil.disk_usage("/")

	print(f"Total: {total // (2**30)} GB"
	print(f"Used: {used // (2**30)} GB")
	print(f"Free {free //(2**30)} GB")
```

This is useful in server monitoring.

## IMP Topics
1. Variables
2. Data Types
3. input/Ouput
4. Conditions ( if )
5. loops
6. functions
7. lists and dictionaries
8. file handling
9. exception handling
10. modules
11. Running Linux commands with oython
12. APU requests
13. Automation scripts



Tips: while learning python, dont just solve coding problems instead think what real task can i sutomate

