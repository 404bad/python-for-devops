# a decorator in python is a fucntion that modifies or extends another function without changing its actual code 
# it is used heavily used in automation, web grameworks, loggin, authentication, timing, retries, and DevOps tooling

def logger(func):

    def wrapper():
        print("Running function")
        func()
        print("Function ended")

    return wrapper

@logger
def deploy():
    print("Deploying")

deploy()

# @logger is actually the shorthand for: deploy = logger(deploy)

# decorator with arguments
def logger1(func):

    def wrapper(*args, **kwargs):
        print("Running function")
        return func(*args, **kwargs)

    return wrapper

@logger1
def greet(name):
    print(f"Hello {name}")

greet("Kailash")

# Why *args and **kwargs?

#They allow the decorator to work with ANY function.
