import json
def addHost(name, address):
    a_dictionary = {name: address}
    with open("hosts.json", "r+") as file:
        data = json.load(file)
        data.pop(name, None)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
    return name + " added"
