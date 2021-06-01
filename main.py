import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import configparser
from frontend.windows.MainMenu import MainMenu

if not os.path.exists('data'):
    os.mkdir('data')

if not os.path.exists('data/owned.json'):
    f = open("data/owned.json", "w")
    f.write("[]")
    f.close()
else:
    f = open("data/owned.json", "r")
    line = f.readline()
    f.close()
    if not line:
        f = open("data/owned.json", "w")
        f.write("[]")
        f.close()


root = tk.Tk()
app = MainMenu(master=root)

config = configparser.ConfigParser()
config.read('data/config.conf')
api_key = config['API']['API_KEY']
if api_key == 'ENTER-API-KEY-HERE':
    api_key = simpledialog.askstring("API Key", "Enter API key from https://dev.pokemontcg.io/")
    if api_key:
        config['API']['API_KEY'] = api_key
        with open('data/config.conf', 'w') as f:
            config.write(f)
    else:
        messagebox.showerror('No api key', 'App needs api key to work properly')
        exit()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
