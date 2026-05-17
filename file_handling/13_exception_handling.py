# exception handling with file is very importat

try:
    with open("test.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
