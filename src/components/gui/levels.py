import customtkinter as ctk
import PIL
from PIL import Image
from src.assets.constant import constants
from src.assets.font.fonts import *


class Levels(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(x=0,y=0, relwidth=1, relheight=1)
        self.configure(bg_color=constants.BACKGROUND_COLOR, 
                    fg_color=constants.BACKGROUND_COLOR,
                    border_color="white", border_width=2,)
        
        self.controller = controller
        self.widgets()
        
        
    def widgets(self):
        
        # Title ------------------------------------------------------------------
        title_label = ctk.CTkButton(self, text="SELECCIONÁ MODO DE JUEGO", 
                                    font=get_LOWERCASE(42), text_color="white",
                                    hover=False, fg_color=constants.BACKGROUND_COLOR,
                                    border_color="white", border_width=2,
                                    width=600, height=60,)
        title_label.place(x=constants.WIDTH/2, y=constants.HEIGHT/2-420, anchor="center")
        
        # Levels ------------------------------------------------------------------
        levels_image = Image.open("src/assets/img/niveles.png")
        levels_image = levels_image.resize((128,128))
        levels_image = ctk.CTkImage(light_image=levels_image, size=(128*1.7,128*1.7))
        self.levels_button = ctk.CTkButton(self, text="NIVELES",
                                    font=get_LOWERCASE(48), text_color="white",
                                    fg_color=constants.BACKGROUND_COLOR,
                                    hover_color=constants.COLOR_BLUE,
                                    border_color="white", border_width=2,
                                    width=300, height=50,
                                    image=levels_image, compound="top")
        self.levels_button.place(x=constants.WIDTH/2-175, y=constants.HEIGHT/2-180, anchor="center")
        
        
        free_image = Image.open("src/assets/img/libre.png")
        free_image = free_image.resize((128,128))
        free_image = ctk.CTkImage(light_image=free_image, size=(128*1.7,128*1.7))
        self.free_button = ctk.CTkButton(self, text="LIBRE",
                                    font=get_LOWERCASE(48), text_color="white",
                                    fg_color=constants.BACKGROUND_COLOR,
                                    hover_color=constants.COLOR_BLUE,
                                    border_color="white", border_width=2,
                                    width=300, height=50,
                                    image=free_image, compound="top")
        self.free_button.place(x=constants.WIDTH/2+175, y=constants.HEIGHT/2-180, anchor="center")
        
        versus_image = Image.open("src/assets/img/versus.png")
        versus_image = versus_image.resize((128,128))
        versus_image = ctk.CTkImage(light_image=versus_image, size=(128*1.7,128*1.7))
        self.versus_button = ctk.CTkButton(self, text="VERSUS",
                                    font=get_LOWERCASE(48), text_color="white",
                                    fg_color=constants.BACKGROUND_COLOR,
                                    hover_color=constants.COLOR_BLUE,
                                    border_color="white", border_width=2,
                                    width=300, height=50,
                                    image=versus_image, compound="top")
        self.versus_button.place(x=constants.WIDTH/2-175, y=constants.HEIGHT/2+130, anchor="center")
        
        
        other_image = Image.open("src/assets/img/otro.png")
        other_image = other_image.resize((128,128))
        other_image = ctk.CTkImage(light_image=other_image, size=(128*1.7,128*1.7))
        self. other_button = ctk.CTkButton(self, text="NO DISPO",
                                    font=get_LOWERCASE(48), text_color="white",
                                    fg_color=constants.BACKGROUND_COLOR,
                                    hover_color=constants.COLOR_BLUE,
                                    border_color="white", border_width=2,
                                    width=300, height=50,
                                    image=other_image, compound="top")
        self.other_button.place(x=constants.WIDTH/2+175, y=constants.HEIGHT/2+130, anchor="center")
        
        self.back_button = ctk.CTkButton(self, text="ATRÁS",
                                    font=get_LOWERCASE(48), text_color="white",
                                    fg_color=constants.BACKGROUND_COLOR,
                                    hover_color=constants.COLOR_BLUE,
                                    border_color="white", border_width=2,
                                    width=300, height=50,
                                    command=lambda: self.controller.show_frame("Menu"))
        self.back_button.place(x=constants.WIDTH/2, y=constants.HEIGHT/2+380, anchor="center")
