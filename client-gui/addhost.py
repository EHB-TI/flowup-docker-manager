import requests, os, sys
import hashlib, time

SERVER_HOST = "10.3.56.6:5432"

def tokenGenerator():
    h = hashlib.sha256()
    timing = str(round(time.time()))
    salt = timing[:-2]
    h.update(bytes(salt, 'utf-8'))
    return h.hexdigest()

def post(name, host):
    resp = requests.get(f"http://{SERVER_HOST}/{name}${host}/{tokenGenerator()}")
    return resp.content.decode("utf-8")

if len(sys.argv) < 3:
    print("not enough arguments")
else:
    name = sys.argv[1]
    host = sys.argv[2]
    print(post(name,host))



