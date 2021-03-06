import docker, os

ARG_LIST = ['restart', 'stop', 'start']
client = docker.from_env()

def showContainers():
    res = ""
    if client.containers.list(all=True):
        for container in client.containers.list(all=True):
            res += container.name + " -> "+container.status + '\n'
        return res
    else:
        return "No running container"

def restartAllContainers(action):
    if client.containers.list(all=True):
        for container in client.containers.list(all=True):
            command = "docker {} {}".format(action, str(container.id)[:12]) 
            os.system(command)
        return "{} done".format(action)
    else:
        return "No running container"