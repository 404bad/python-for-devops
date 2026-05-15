#Dictionaries
# A dictionary stores data in key: value

server = {
	"name": "web-server",
	"ip": "192.168.1.10",
	"os": "ubuntu"
}

print(server)

# Why dictionaries are important in DevOps
# insfrsstructure data is usuallly structured like:
# serve name, ip addresses, envirenments, credentials, cinfigurations
# dictionaries help organize this

# Accessing Dictionary values

print(server["name"])
print(server["ip"])

# Adding new values
server["username"]: "kailash"

print(server)


# Looping throught dictionaries

for key, value in server.items():
  print(key, ":", value)

