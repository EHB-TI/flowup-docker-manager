from flask import send_file, send_from_directory, safe_join, abort, Flask
from generator import tokenGenerator
from execute import exec_command, restartAllContainers
import os, time, sys
app = Flask(__name__)

ARG_LIST = ['restart', 'stop', 'start']

@app.route("/<token>/<file_name>")
def get_file(token, file_name):
    if(token == tokenGenerator()):
        if file_name not in ARG_LIST:
            result = exec_command(file_name)
            return result
        else:
            result = restartAllContainers(file_name)
            return result
    else:
        return "bad request"

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        sys.exit(0)
