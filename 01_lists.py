# Lists in python
# A list stored multiple values in a single variable.
# the values can be of multiple types
# but in array is a list of only similar rtypes

servers = ["nginx","docker","jenkins"]
print(servers)


# why list are useful in DevOps
# suppose we want to: restart multiple servers, deploy to multiple environements. install many packages, loop thriugh containers
# list makes this easy

# Accessing List items

print(servers[0])
print(servers[1])


# Adding Items to a list
# 1. using append()
servers.append("kubernetes")
print(servers)

# 2. using insert()

servers.insert(1,"kubernetes")
print(servers)


# Removing item from list
# .remove() deleted only the first occurence of the value.

servers.remove("kubernetes")
print(servers)


# to remve all occurrences
servers = [server for server in servers if server != "kubernetes"]
print(servers)

# remove by index

del servers[1]
print(servers)

# Looping through a list
# this is very important in devops

for server in servers:
  print("Deploying to", server)


# Example : Installing packages

packages= ["nginx","docker.io","git"]

for package in packages:
  print (f"Installing {package}")
