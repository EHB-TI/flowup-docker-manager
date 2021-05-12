import os
import os.path
import docker

ARG_LIST = ['restart', 'stop', 'start']
client = docker.from_env()

def isWindows():
    if os.name == "nt":
        return True
    else:
        return False

def fileExists(action):
    end = "bat" if isWindows() else "sh"
    path = "./scripts/"
    if os.path.isfile(f"{path}{action}.{end}"):
        return True
    else:
        return False
def exec_command(action):
        if fileExists(action):
            if isWindows():
                command = "cd scripts & {}.bat".format(action)
            else:
                command = "bash ./scripts/{}.sh".format(action)
            returned_output = os.popen(command).read()
            return returned_output
        else:
            if action[0] == '=':
                command = action[1:].replace("%", " ")
                command = command.replace("+", ".")
                command = command.replace("^", "/")

                returned_output = os.popen(command).read()
                return returned_output
            else:
                return "No matching script found"

def restartAllContainers(action):
    if client.containers.list(all=True):
        for ids in client.containers.list(all=True):
            command = "docker {} {}".format(action, str(ids.id)[:12]) 
            os.system(command)
        return "{} done".format(action)

    else:
        return "No running container"