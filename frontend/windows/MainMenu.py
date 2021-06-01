import tkinter as tk
from tkinter import messagebox


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gotta catch 'em all!")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = "Pokémon collection"
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        self.stats_button = tk.Button(self)
        self.stats_button["text"] = "Your stats"
        self.stats_button["command"] = lambda: print("stats")
        self.stats_button.pack(side="top", pady=20)

        self.collection_button = tk.Button(self)
        self.collection_button["text"] = "Collection"
        self.collection_button["command"] = self.say_hi
        self.collection_button.pack(side="top", pady=20)

    def say_hi(self):
        print("hi there, everyone!")