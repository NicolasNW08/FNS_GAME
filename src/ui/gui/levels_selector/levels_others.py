from src.core.constant import constants
import customtkinter as ctk

class Others(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        self.controller = controller
        self.widgets()
        
    def widgets(self):
        asd = ctk.CTkLabel(self, text="Others")
        asd.place(x=constants.WIDTH/2, y=constants.HEIGHT/2, anchor="center")