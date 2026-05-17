#count errors in log file

count = 0
with open ("app.log","r") as file:
    for line in file:
        if "ERROR" in line:
            count+=1

print(count)
