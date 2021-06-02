import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import backend.GetData as GetData


IMAGES_CONTAINER = []


class GameWindow(tk.Frame):
    def __init__(self, master=None, set_id=None):
        super().__init__(master)
        global IMAGES_CONTAINER
        IMAGES_CONTAINER = []
        self.master = master
        self.cards = []
        temp = GetData.get_cards_from_set(set_id)
        for c in temp:
            if c["supertype"] == "Pokémon":
                self.cards.append(c)
        self.master.title(self.cards[0]["set"]["name"] + ': game')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.chosen = random.choice(self.cards)
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = 'Guess the name'
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        im = GetData.get_img(self.chosen["images"]["small"])
        im2 = im.crop([21, 36, 222, 168])
        IMAGES_CONTAINER.append(ImageTk.PhotoImage(im2, master=self))
        self.image_label = tk.Label(self, image=IMAGES_CONTAINER[0])
        self.image_label.pack(side="top")
        self.textbox = tk.Text(self, height=1, width=50)
        self.textbox.pack(side="top", padx=10, pady=5)
        self.submit_b = tk.Button(self, text='Submit', command=lambda: self.submit_name())
        self.submit_b.pack(side="top", pady=2)
        self.show_name = tk.Button(self, text='Show name', command=lambda: messagebox.showinfo('Card name', self.chosen['name']))
        self.show_name.pack(side="top", pady=10)

    def submit_name(self):
        name = self.textbox.get("1.0", "end-1c")
        if name.upper() == self.chosen["name"].upper():
            for child in self.winfo_children():
                child.destroy()
            IMAGES_CONTAINER.pop()
            self.create_widgets()
        else:
            messagebox.showwarning('Wrong name', 'You entered wrong name')
