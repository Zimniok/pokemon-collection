import tkinter as tk
import backend.GetData as GetData
import backend.SetData as SetData
from frontend.windows.CardInfoWindow import CardInfoWindow


def show_card_details(card):
    card_info_root = tk.Toplevel()
    card_info = CardInfoWindow(master=card_info_root, card=card)
    card_info.pack(side="top", fill="both", expand=True)
    card_info_root.mainloop()


class CardsWindow(tk.Frame):
    def __init__(self, master=None, set_id=None, cards=None):
        super().__init__(master, width=600, height=415)
        self.master = master
        if not cards:
            if not set_id:
                self.cards = []
            else:
                self.cards = GetData.get_cards_from_set(set_id=set_id)
        else:
            self.cards = cards
        self.master.title("Cards list")
        self.pack()
        self.create_widgets()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = "Cards"
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        self.title_bar = tk.Frame(self)

        self.data_order = tk.Label(self.title_bar, text='Data order: ')
        self.data_order.grid(row=0, column=0)
        self.title_name_lable = tk.Label(self.title_bar, text='Set name')
        self.title_name_lable.grid(row=0, column=1)
        self.title_number_label = tk.Label(self.title_bar, text='Card number')
        self.title_number_label.grid(row=0, column=2)
        self.title_card_name_label = tk.Label(self.title_bar, text='Card name')
        self.title_card_name_label.grid(row=0, column=3)

        self.title_bar.pack(side="top", padx=10, fill='x')

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, pady=5, padx=10)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.owned_list = []

        for i in range(len(self.cards)):
            self.owned_list.append(tk.IntVar())
            self.owned_list[i].set(self.cards[i]["owned"])
            self.set_name_label = tk.Label(self.frame, text=self.cards[i]["set"]["name"], bg='white')
            self.set_name_label.grid(sticky="W", row=i, column=0)
            self.number_label = tk.Label(self.frame, text=self.cards[i]["number"], bg='white')
            self.number_label.grid(sticky="W", row=i, column=1)
            self.name_label = tk.Label(self.frame, text=self.cards[i]["name"], bg='white')
            self.name_label.grid(sticky="W", row=i, column=2)
            self.info_button = tk.Button(self.frame, text="Details", command=lambda card=self.cards[i]: show_card_details(card))
            self.info_button.grid(sticky="E", row=i, column=3)
            self.owned_checkbox = tk.Checkbutton(self.frame, text="Owned", variable=self.owned_list[i], command=lambda id=self.cards[i]["id"], i=i: self.save_owned(id, i))
            self.owned_checkbox.grid(sticky='E', row=i, column=4)
        self.master.geometry('600x415')

    def save_owned(self, id, i):
        SetData.set_owned_state(id, self.owned_list[i].get())
