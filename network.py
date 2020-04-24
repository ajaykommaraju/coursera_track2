import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost

def check_connectivity():
    request = requests.get("http://www.google.com")
    return request

print(check_localhost())
print(check_connectivity())