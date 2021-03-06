#Author: Nabil Lahssini
import tkinter as tk
from tkinter import ttk
import os, sys
import hashlib, time
import requests
ARG_LIST = ['restart', 'stop', 'start', 'list']

if len(sys.argv) < 2:
    SERVER_HOST = "10.3.56.6:5432"
else:
    if len(sys.argv[1].split('.')) < 4:
        print("Bad address")
        sys.exit(1)
    else:
        SERVER_HOST = sys.argv[1]

def executeCommand(host, action):
    if action not in ARG_LIST:
        return "Bad request"
    else:
        try:
            resp = requests.get(f"http://{SERVER_HOST}/{host}/{action}/{tokenGenerator()}")
            return resp.content.decode("utf-8")
        except:
            return "Host is unreachable"

def tokenGenerator():
    h = hashlib.sha256()
    timing = str(round(time.time()))
    salt = timing[:-2]
    h.update(bytes(salt, 'utf-8'))
    return h.hexdigest()

def sendRequest():
    host = ent_host.get()
    action = ent_command.get()
    lbl_result["text"] = executeCommand(host, action)

def handle_keypress(event):
    sendRequest()

# Set-up the window
window = tk.Tk()
window.iconbitmap("./ressources/icon.ico")
window.title("Container manager")
window.resizable(width=True, height=True)
window.minsize(width=350, height=100)
window.bind("<Return>", handle_keypress)
# widget and label in it
frm_entry = tk.Frame(master=window)
lbl_host = tk.Label(master=frm_entry, text="Host ")
n = tk.StringVar()
#ent_host = tk.Entry(master=frm_entry, width=50)
ent_host = ttk.Combobox(window,width=50)
ent_host['values'] = ('monitor', 
                          'uuidmaster',
                          'office',)
ent_command = ttk.Combobox(window,width=50)
ent_command['values'] = ('list', 
                          'start',
                          'stop',
                          'restart',)
lbl_result = tk.Label(master=window, text="status")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
lbl_host.grid(row=1, column=0, padx=10)
ent_host.grid(row=1, column=0,padx=10, pady=10)
ent_command.grid(row=2, column=0,padx=10, pady=10)
ent_command.current(0)

# Create the conversion Button and result display Label
btn_execute = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=sendRequest
)

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_execute.grid(row=3, column=0, pady=10)
lbl_result.grid(row=4, column=0, padx=10)

# Run the application
window.mainloop()