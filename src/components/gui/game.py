import customtkinter as ctk

from src.assets.constant import constants

class Levels(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x=0,y=0, relwidth=1, relheight=1)
        self.configure(bg_color=constants.BACKGROUND_COLOR, 
                    fg_color=constants.BACKGROUND_COLOR,
                    border_color="white", border_width=2,)
        
        self.controller = controller
        
        

