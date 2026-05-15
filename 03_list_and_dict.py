servers = [
    {"name": "web1", "ip": "192.168.1.10"},
    {"name": "web2", "ip": "192.168.1.11"}
]

for server in servers:
    print(server["name"], server["ip"])
