import tkinter as tk
import backend.GetData as GetData
from frontend.windows.SetInfoWindow import SetInfoWindow
from frontend.windows.CardsWinodw import CardsWindow
from frontend.windows.GameWindow import GameWindow


def show_set_info(set):
    set_info_root = tk.Toplevel()
    set_info = SetInfoWindow(master=set_info_root, set=set)
    set_info.pack(side="top", fill="both", expand=True)
    set_info_root.mainloop()


def show_cards(set_id):
    cards_list_root = tk.Toplevel()
    cards_list = CardsWindow(master=cards_list_root, set_id=set_id)
    cards_list.pack(side="top", fill="both", expand=True)
    cards_list_root.mainloop()


def show_game(set_id):
    game_root = tk.Toplevel()
    game = GameWindow(master=game_root, set_id=set_id)
    game.pack(side="top", fill="both", expand=True)
    game_root.mainloop()


class CollectionWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=600, height=445)
        self.master = master
        self.master.title("Collection")
        self.pack()
        self.create_widgets()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = "Pokémon collection"
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        self.title_bar = tk.Frame(self)

        self.data_order = tk.Label(self.title_bar, text='Data order: ')
        self.data_order.grid(row=0, column=0)
        self.title_name_lable = tk.Label(self.title_bar, text='Set name,')
        self.title_name_lable.grid(row=0, column=1)
        self.title_series_label = tk.Label(self.title_bar, text='Series')
        self.title_series_label.grid(row=0, column=2)

        self.title_bar.pack(side="top", padx=10, fill='x')

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, pady=20, padx=10)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.sets_list = []
        all_sets = GetData.all_sets()

        for i in range(len(all_sets)):
            self.set_name = tk.Label(self.frame, text=all_sets[i]["name"], bg='white')
            self.set_name.grid(sticky='W', row=i, column=0, padx=20)
            self.series = tk.Label(self.frame, text=all_sets[i]["series"], bg='white')
            self.series.grid(sticky='W', row=i, column=1, padx=20)
            self.info_button = tk.Button(self.frame, text="info", command=lambda set=all_sets[i]: show_set_info(set))
            self.info_button.grid(sticky="E", row=i, column=2, padx=20)
            self.cards_button = tk.Button(self.frame, text="cards", command=lambda set_id=all_sets[i]["id"]: show_cards(set_id))
            self.cards_button.grid(row=i, column=3)
            self.game_button = tk.Button(self.frame, text="game", command=lambda set_id=all_sets[i]["id"]: show_game(set_id))
            self.game_button.grid(row=i, column=4, padx=20)
        self.master.geometry('600x445')

