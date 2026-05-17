# Python funtions for devops s ripting
# Functions are one of the most important things in dvops scripting becuse they help us: to avoid repeting code, organize automations scripts, reuse logic, debug faster, make scripts production ready

# In real DevOps work, almost every python automation used functions.

# function is a resusable block of code.
# instead of writing the same commands again and again , you put them iside a funciton and call it whenver needed.

def greet():
    print("Hello DevOps Engineer")

greet()

def deploy():
     print("Deploying application...")

deploy()

# parameters and arguments
# functioncan accepst input

def greet1(name):
    print(f"Hello {name}")

greet1("kailash")

# Parameter is a variable written in function definition def greet(name), the name is the placeholder that will receive a value. while the argument is the actula aluse pssed when calling the function. print("kailash")

# multiple parameters

def add(a,b):
    print(a+b)
add(5,3)

# Retrun and print
# This is very important for DevOps scripting.
# print () only shows output. while return sends value back
# use return in real scripts

# why return matters in DevOps

# imagine a scenario of chekcing disk usage

# bad

def check_disk():
    print("80%")

# good

def good_check_disk():
    return "80%"

usage = good_check_disk()

if usage == "80%":
    print ("Disk almmost full")

# default parameter
def deploy1(env="dev"):
    print(f"Deploying to {env}")

deploy1()


# Keyword arguments

def create_vm(name, cpu, ram):
    print(name, cpu, ram)

create_vm(ram="8GiB", cpu=4, name="cluster management server")

# positional arguments: order matters

def user(name,age):
    print(name,age)

user("kailash",23)

# Arbitary Arguments (*args)
# used when we dont knnow how many inputs will come.

def install_packages(*packages):
    for package in packages:
        print(f"Installing {package}")

install_packages("nginx","docker","git")

# Keyword Arbitrary Arguments (**kwargs)

# used for dynamic configs.

def server_info(**details):
    for key,value  in details.items():
        print(key,value)

server_info(name="web1", ip="1.1.1.1", os="ubuntu")

# local and global variables

# local variable: exists only inside function.

def test():
    x = 10
    print(x)

test()

# x exists only inside function

# gloabl variable is accesible everywhwre

env = "production"

def deploy3():
    print (env)

deploy3()



# returing multipe values

def server():
    return "web1","192.168.1.10"

name, ip = server()

print(name)
print(ip)

# nested functions
#function inside another function.

def outer():

    def inner():
        print("Inner function")

    inner()

outer()

# Used less in beginner ecripting but common in frameworks.

# lambda functions: smalle one-line functions

square = lambda x: x*x
print(square(5))


# Recursion: function calling itself

def countdown(n):
    if n == 0:
        return 

    print(n)
    countdown(n-1)

countdown(5)


# Docstrings: Documentation inside function

def deploy4():
    """
    Deploy application to kubernetes
    """

    print("Deploying..")

# good fro teans and prodcution scripts

# types hints: very usefull in professionla DevOps python

def add1(a: int, b: int) -> int:
    return a+b


