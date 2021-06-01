import tkinter as tk
from PIL import ImageTk
import backend.GetData as GetData


class SetInfoWindow(tk.Frame):
    def __init__(self, master=None, set_id=None, set=None):
        super().__init__(master)
        self.master = master
        if not set:
            self.set = GetData.get_set_info(set_id)
        else:
            self.set = set
        self.master.title("Set " + self.set["name"] + " info")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, font=("Roboto", 30))
        self.title["text"] = self.set["name"]
        self.title["padx"] = 20
        self.title["pady"] = 20
        self.title.pack(side="top")

        self.info_frame_background = "white"
        self.info_frame = tk.Frame(self, background=self.info_frame_background)

        # self.first_line = tk.Frame(self.info_frame, background=self.info_frame_background)
        # self.symbol_text = tk.Label(self.first_line, text="Symbol:", bg=self.info_frame_background)
        # self.symbol_text.pack(side="left")
        # pimg = GetData.get_img(self.set["images"]["symbol"])
        # img = ImageTk.PhotoImage(pimg, master=self.first_line)
        # symbol_img = tk.Label(self.first_line, image=img)
        # symbol_img.pack(side="left")
        # self.first_line.pack(side="top")

        # self.second_line = tk.Label(self.info_frame, background=self.info_frame_background)
        # self.name_label = tk.Label(self.second_line, text=str("Name: " + self.set["name"]), bg=self.info_frame_background)
        # self.name_label.pack(side="left")
        # self.series_label = tk.Label(self.second_line, text=("Series: " + self.set["series"]), bg=self.info_frame_background)
        # self.series_label.pack(side="left", padx=20)
        # self.second_line.pack(side="top", padx=20, pady=10, fill='x')
        #
        # self.third_line = tk.Frame(self.info_frame, background=self.info_frame_background)
        # self.printed = tk.Label(self.third_line, text=("Total printed: " + str(self.set["printedTotal"])), bg=self.info_frame_background)
        # self.printed.pack(side="left")
        # self.third_line.pack(side="top", padx=20, pady=10, fill='x')
        #
        # self.fith_line = tk.Frame(self.info_frame, background=self.info_frame_background)
        # self.ptcgo_code = tk.Label(self.fith_line, text="PTCGO code: " + str(self.set["ptcgoCode"]),
        #                            bg=self.info_frame_background)
        # self.ptcgo_code.pack(side="left")
        # self.fith_line.pack(side="top", padx=20, pady=10, fill='x')
        #
        # self.fourth_line = tk.Frame(self.info_frame, background=self.info_frame_background)
        # self.release_date = tk.Label(self.fourth_line, text="Release date: "+str(self.set["releaseDate"]), bg=self.info_frame_background)
        # self.release_date.pack(side="left")
        # self.update_date = tk.Label(self.fourth_line, text="Last updated: "+str(self.set["updatedAt"]), bg=self.info_frame_background)
        # self.update_date.pack(side="right")
        # self.fourth_line.pack(side="top", padx=20, pady=10, fill='x')

        self.name_label = tk.Label(self.info_frame, text=str("Name: " + self.set["name"]),
                                   bg=self.info_frame_background)
        self.name_label.grid(row=0, column=0)
        self.series_label = tk.Label(self.info_frame, text=("Series: " + self.set["series"]),
                                     bg=self.info_frame_background)
        self.series_label.grid(row=0, column=1)
        self.printed = tk.Label(self.info_frame, text=("Total printed: " + str(self.set["printedTotal"])),
                                bg=self.info_frame_background)
        self.printed.grid(row=1, column=0)
        self.ptcgo_code = tk.Label(self.info_frame, text="PTCGO code: " + str(self.set["ptcgoCode"]),
                                   bg=self.info_frame_background)
        self.ptcgo_code.grid(row=2, column=0)
        self.release_date = tk.Label(self.info_frame, text="Release date: " + str(self.set["releaseDate"]),
                                     bg=self.info_frame_background)
        self.release_date.grid(row=3, column=0)
        self.update_date = tk.Label(self.info_frame, text="Last updated: " + str(self.set["updatedAt"]),
                                    bg=self.info_frame_background)
        self.update_date.grid(row=3, column=1)

        self.info_frame.pack(side="top", fill="both", padx=20, pady=20)
