with open("/var/log/syslog","r") as file:
    for line in file:
        print(line)
