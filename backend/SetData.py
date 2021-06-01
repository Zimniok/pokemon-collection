import json
import tkinter as tk
from tkinter import messagebox


def set_owned_state(id, owned):
    data = []
    try:
        f = open('data/owned.json')
        data = json.load(f)
        f.close()
    except FileNotFoundError:
        messagebox.showerror('File not found', 'File owned.json has not been found in the data folder.')
        return

    is_done = False
    for card in data:
        if card["id"] == id:
            card["owned"] = owned
            is_done = True
            break
    if not is_done:
        data.append({"id": id, "owned": owned})
    f = open('data/owned.json', 'w')
    json.dump(data, f)
    f.close()
