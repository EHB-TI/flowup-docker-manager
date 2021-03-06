from flask import Flask
from req import execute_request
from manageHosts import addHost
from generator import tokenGenerator
import os, time
app = Flask(__name__)
PORT = os.getenv('PORT', "5000")
app.config["DEBUG"] = True

@app.route("/<host>/<action>/<token>")
def main_exec(host, token, action):
    if(token == tokenGenerator()):
        return execute_request(host,action)
    else:
        return "bad request"

@app.route("/<name_address>/<token>")
def add_host(name_address, token):
    what = name_address.split('$')
    name = what[0]
    address = what[1]
    if(token == tokenGenerator()):
        return addHost(name,address)
    else:
        return "Bad request"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=PORT)

