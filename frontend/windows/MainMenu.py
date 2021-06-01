import tkinter as tk
from tkinter import simpledialog, messagebox
import backend.GetData as GetData
from frontend.windows.CollectionWindow import CollectionWindow
from frontend.windows.CardsWinodw import CardsWindow


def show_stats():
    messagebox.showinfo('Stats', 'You have collected: ' + str(GetData.get_number_of_owned_cards()) + ' cards!')


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
        self.stats_button["command"] = lambda: show_stats()
        self.stats_button.pack(side="top", pady=20)

        self.collection_button = tk.Button(self)
        self.collection_button["text"] = "Collection"
        self.collection_button["command"] = self.go_to_collection
        self.collection_button.pack(side="top", pady=20)

        self.owned_button = tk.Button(self)
        self.owned_button["text"] = "Owned cards"
        self.owned_button["command"] = self.go_to_owned
        self.owned_button.pack(side="top", pady=20)

        self.find_card_button = tk.Button(self)
        self.find_card_button["text"] = "Find a card"
        self.find_card_button["command"] = self.serach_card_win
        self.find_card_button.pack(side="top", pady=20)

        self.author_button = tk.Button(self)
        self.author_button["text"] = "Author"
        self.author_button["command"] = lambda: messagebox.showinfo('Author', 'Marcin Pierzchała')
        self.author_button.pack(side="top", pady=20)

    def go_to_collection(self):
        collection_root = tk.Toplevel()
        collection = CollectionWindow(master=collection_root)
        collection.pack(side="top", fill="both", expand=True)
        collection.mainloop()

    def go_to_owned(self):
        if not GetData.get_number_of_owned_cards():
            messagebox.showinfo('No cards', 'You do not own any cards')
        else:
            owned_root = tk.Toplevel()
            owned = CardsWindow(master=owned_root, cards=GetData.get_owned_cards())
            owned.pack(side="top", fill="both", expand=True)
            owned_root.mainloop()

    def serach_card_win(self):
        card_name = simpledialog.askstring("Card search", "Enter a fragment of a name or full name of a card")
        if card_name:
            card_info_root = tk.Toplevel()
            card_info = CardsWindow(master=card_info_root, cards=GetData.search_card_by_name(card_name))
            card_info.pack(side="top", fill="both", expand=True)
            card_info_root.mainloop()

