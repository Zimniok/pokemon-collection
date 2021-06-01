import os
import tkinter as tk
from tkinter import messagebox
from frontend.windows.MainMenu import MainMenu

if not os.path.exists('../data'):
    os.mkdir('../data')

root = tk.Tk()
app = MainMenu(master=root)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
