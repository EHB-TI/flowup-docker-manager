from flask import send_file, send_from_directory, safe_join, abort, Flask
from generator import tokenGenerator
from execute import restartAllContainers, showContainers
import os, time, sys
app = Flask(__name__)

ARG_LIST = ['restart', 'stop', 'start', 'list']

@app.route("/<token>/<action>")
def get_file(token, action):
    if action not in ARG_LIST:
        return "bad request"
    else:
        if action == 'list':
            return showContainers()
        else:
            return restartAllContainers(action)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        sys.exit(0)
