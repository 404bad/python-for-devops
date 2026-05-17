# Generate reports

cpu= "70%"
memory = "60%"

with  open ("report.txt","w") as file:
    file.write(f"CPU Usage: {cpu}\n")
    file.write(f"Memory Usage: {memory}\n")


