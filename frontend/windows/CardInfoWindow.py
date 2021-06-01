import tkinter as tk
import backend.GetData as GetData
from PIL import ImageTk


IMAGES_CONTAINER = []


class CardInfoWindow(tk.Frame):
    def __init__(self, master=None, card_id=None, card=None):
        super().__init__(master)
        self.master = master
        if not card:
            self.card = GetData.get_set_info(card_id)
        else:
            self.card = card
        self.master.title("Card " + self.card["name"] + " info")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = self.card["name"]
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        self.info_frame_background = "white"
        self.info_frame = tk.Frame(self, background=self.info_frame_background)

        self.set_info_frame = tk.Frame(self.info_frame, background='#cfcfcf')

        self.set_info_title = tk.Label(self.set_info_frame, text="Set info", font=("Roboto", 12), bg='#cfcfcf')
        self.set_info_title.grid(row=0, column=0, columnspan=2)
        self.set_info_name = tk.Label(self.set_info_frame, text="Name: "+self.card["set"]["name"], bg='#cfcfcf')
        self.set_info_name.grid(row=1, column=0)
        self.set_info_series = tk.Label(self.set_info_frame, text="Series: "+self.card["set"]["series"], bg='#cfcfcf')
        self.set_info_series.grid(row=1, column=1)

        self.set_info_frame.grid(sticky="N", columnspan=2, row=0, column=0, padx=10, pady=10)

        self.name_label = tk.Label(self.info_frame, bg=self.info_frame_background, text="Name: "+self.card["name"])
        self.name_label.grid(row=1, column=0, sticky="W")
        self.number_label = tk.Label(self.info_frame, bg=self.info_frame_background, text="Number: "+self.card["number"])
        self.number_label.grid(row=2, column=0, sticky="E")
        self.types_label = tk.Label(self.info_frame, bg=self.info_frame_background, text="Types: "+' '.join(self.card["types"]))
        self.types_label.grid(row=3, column=0, sticky="W")
        if "tcgplayer" in self.card:
            self.price_label = tk.Label(self.info_frame, bg=self.info_frame_background, text="Prices:")
            self.price_label.grid(row=4, column=0, sticky="W")
            self.price_frame = tk.Frame(self.info_frame, background=self.info_frame_background)
            i = 0
            for key in self.card["tcgplayer"]["prices"]:
                self.price_name = tk.Label(self.price_frame, bg=self.info_frame_background, text=key)
                self.price_name.grid(row=i, column=0, sticky="W", padx=10)
                i += 1
                for price_level in self.card["tcgplayer"]["prices"][key]:
                    self.price_level = tk.Label(self.price_frame, bg=self.info_frame_background, text=price_level+": "+str(self.card["tcgplayer"]["prices"][key][price_level])+"$")
                    self.price_level.grid(row=i, column=1, sticky="W")
                    i += 1
            self.price_frame.grid(row=4, column=0, columnspan=2)
        self.info_frame.pack(side="left", fill="both", padx=20, pady=20)
        IMAGES_CONTAINER.append(GetData.get_img(self.card["images"]["small"]))
        IMAGES_CONTAINER[0] = ImageTk.PhotoImage(IMAGES_CONTAINER[0], master=self)
        self.image_label = tk.Label(self, image=IMAGES_CONTAINER[0])
        self.image_label.pack(side="left")
