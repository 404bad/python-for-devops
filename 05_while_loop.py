# a while loop runs until a condition becomes false.

#syntac
# while condition:
#     code

# python doesnot have do while loop

count=1
while count <=5:
    print(count)
    count+=1


# wait untill servie starts

service_running = False

while not service_running:
    print("Checking service...")

    # simulate service becoming active
    service_running = True

print("Service started")

# use din kubernetes readiness checks, docker container montiring, cicd waiting logic

# infinite monitoring loop

while True:
    print("Monitoring server....")

# while true create an infinte loop

# used for monitoring tools, daemons, log watches. It usually stopped with ctrl + c

# summary
# for loops are used for iterating over collections like serve, pods, or files. while loops are used when automation needs to continue untill a cndition is met, such as waiting for a service to become healthy.


