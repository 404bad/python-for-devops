# Exception Handling

Exception handling in python is very important in DevOps scripting because scripts often dela with:
- files
- servers
- APIs
- Docker/Kubernetes commands
- cloud resources
- automation pipelines

Things faill all the time in real systems, so your script should handle failures gracefully instead of crashing.

## what is an exception?

An exception is an error that happens while the program is running.

```python
    x=10/0
```
ZeroDivisionError

without exception hanlding, the script stops immediately.

## Basic try-except

```python
    try:
        x = 10/0
    except:
        print("Something went wrong.
```

output: something went wrong

## Catch specific Exception (Best Practice

Instead of catching everything.

```python
    try:
        x= 10/0
    except ZeroDivisionError:
        print("Cannot divide by zero
```

## Common Exception in DevOps

- FileNotFoundError: file missing
- PermissionError: no permission
- ValueError: wrong input
- KeyError: missing dictionary key
- IndexError: invalid list index
- subprocess.CalledProcessError: command failed
- ConnectionError: API/server unreahable
- TimeoutError: operation timed out


## finally block
- finally always run

useful for : closing files, database cleanup, releasing resources

```python
    try:
        file = open ("data.txt")
        
    except FileNotFoundError:
        print("Missing file.")
    finally:
        print("Clean completed")
    
```

## else block

Runs only if NO exception occurs.

```python
    try:
        x = 10 / 2
    except eroDivisionError:
        print("Cannot divide")
    else:
        print("Sucess: ",x)

```

## full structure

```python
    try:
        # risky code

    except SomeError:
        # handle error

    else:
        # runs if success

    finally:
        # always runs
``

## Do not do this often

```py
    except:
        pass
````

why it is bad? it hides real errors, debigging becomes impossible.





## Best practices for DevOps scripts

### good

- catch specific exceptions
- log erros
- use finally for cleanup
- give meaningful error messages
- fail gracefully

### Bad

- Using only except: everywhere
- Ignoring exceptios
- hiding errors to pass
- No logging in automation scripts


## why is exception handling is impotant is DevOps

DevOps scripts interact with infrastructure, APIs, srvers, and files where failures are common. Exception handling prevents automation from crashing unexpextedly and helps with logging, recoery, debugging, and graceful faulire handling.


## most importaat DevOps exception

- FileNotFound
- permissionError
- ValueError
- KeyError
- subprocess.calledProceaaError
- requests.exceptions.Timeout
- requests.exceptions.connectionError
- json.JSONDecodeError


