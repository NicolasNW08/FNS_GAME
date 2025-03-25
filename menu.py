from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import assets.constant.constants as constants
from assets.img.animation.bg_animation import BGAnimation



class gui_menu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("F*king Numbers")
        self.geometry("{}x{}+{}+{}".format(
        constants.WIDTH, constants.HEIGHT,
        int((self.winfo_screenwidth() - constants.WIDTH) / 2),
        int((self.winfo_screenheight() - constants.HEIGHT) / 2)
        ))
        self.resizable(False, False)
        
        self.widgets()


        self.mainloop()
        
    
    def widgets(self):
        # Background -------------------------------------------------------------
        self.bg_label = ttk.Label(self)
        self.bg_label.place(x=-2, y=-2)
        
        self.bg_animation = BGAnimation(self, self.bg_label)
