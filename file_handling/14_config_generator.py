config = """
PORT=8080
ENV=production
DEBUG=False
"""

with open(".env", "w") as file:
    file.write(config)
