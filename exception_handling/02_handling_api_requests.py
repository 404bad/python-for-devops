import requests

try:
    response = requests.get("https://google.com", timeout=3)
    print(response.status_code," = OK")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Cannot connect")
