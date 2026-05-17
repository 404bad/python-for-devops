# log monitoring script

def check_errors(log_file):
    count = 0
    with open (log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                count+=1
    return count

errors = check_errors("app.log")

print(f"Total errors: {errors}")
