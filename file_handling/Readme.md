# file handling in python for DevOps
 file handling is one of the most important in DevOps scripting.

 we use it for: reading coding files, reading logs, writing deployment rerports, editing .rnv files, parsing yaml/json generating backups, automation scripts, CICD outputs

 file handling means opening files, reading files, writing files, mofifying files, deleting files

## opening a file

```python
    open("filename","mode")

    file = open ("text.txt","r")

```

## files modes
 
- r: read
- w: write(overwrites)
- a: append
- x: create new file
- rb: read binary
- wb: write binary

## Reading a file
- read() : reads entire file egL content = file.read()

## why close matters

files use system resiurces. Always close them

bad
```python
    file = open("text.txt","r")

```

good
```file.close()
```

## better way

use with open

```python
    with open ("ttest.txt","r") as file:
        content = file.read()
        print(content)
```

### why better?
- automatially closes file
- safer
- cleaner
- professinal way

### read line by line
 ```python
    with open ("test.txt","r") as file:
        for line in file:
            print(line)
```

used for log files, configs, monitoring

### read line()

reads one line
```python
with open ("test.txt","r") as filed:
 print(file.readline())
 print(file.readline())
```

### read lines

return list.

```python
    with open ("test.txt","r") as file:
        lines = file.readlines()
    print(lines)

```

## writing to a file

"w" mode
```python
    with open("output.txt","w") as file:
        file.write("Hello DevOps")
```

- creates file if not exists. overwrites existing content.

## Append mode
adds data without deleting old content.

```python
    with open ("logs.txt","a") as file:
        file.write("New deployment\n")

```
this is very common in logging.

## create file
 - x mode

```python
    with open("new.txt","x") as file:
        file.write("created")
```

- fails if file already exists.


## writing multiple lines

```python
    lines=[
        "docker\n"
        "kubernetes\n"
        "terraform\n"
]

with open("tools.txt","w") as file:
    file.writelines(lines)
```
## check if file exists

```python
    import os
    if os.path.exists("test.txt"):
        print("file exists")
    else:
        print("Not Found")
```

## delete file

```python
    import os
    os.remove("text.txt")
```

## rename file
```python
    import os
    os.rename("old.txt","new.txt")
```

# working with the directories

## create folder
```python
    os.mkdir("logs")
    os.makedirs("/projects/logs/dev") # nested folders
```
## remove fodler
```python
    os.rmdir("logs")
```
- folder must be empty

## list files in directoy

```python
    import os
    files = os.listdir(".")
    print(files)

```

very useful in automation.

## current working deirectoy

```python
    os.getcwd()

```

## change direcoty

```python
    os.chdir("/home/kailash/projects")
```



## Read huge files efficiently

bad: content = file.read()

good:

```python
    with open ("huge.log","r") as file:
        for line in file:
            print(line)
```

very important for production logs

## file permissions

```python
    import os

os.chmod("script.sh", 0o755)
```
useful in deployemnt automation

## Temporary files

```python
    import tempfile

    temp = tempfile.NamedTemporaryFile()
    print(temp.name)
```


