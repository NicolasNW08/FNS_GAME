from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from assets.animation.dialogue_animation import DialogueAnimator
import assets.constant.constants as constants
from assets.font.fonts import *
import random

from assets.animation.pc_menu_animation import PC_MENUAnimation
from assets.animation.title_animation import TITLEAnimation
from assets.animation.bg_animation import BGAnimation

from language.es_ES import *


class gui_menu(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self)
        self.title("F*king Numbers")
        self.iconbitmap("assets/img/icon.ico")
        self.geometry("{}x{}+{}+{}".format(
        constants.WIDTH, constants.HEIGHT,
        int((self.winfo_screenwidth() - constants.WIDTH) / 2),
        int((self.winfo_screenheight() - constants.HEIGHT) / 2-30)
        ))
        self.resizable(False, False)
        
        self.widgets()


        self.mainloop()
        
    
    def widgets(self):
        # Background -------------------------------------------------------------
        self.bg_label = ctk.CTkLabel(self, text="")
        self.bg_label.place(x=0, y=0)
        
        self.bg_animation = BGAnimation(self, self.bg_label)
        
        
        # Title ------------------------------------------------------------------
        self.title_label = ctk.CTkLabel(self, text="", bg_color="transparent")
        self.title_label.place(x=constants.WIDTH/2, y=constants.HEIGHT/2-380, anchor="center")
        
        self.title_animation = TITLEAnimation(self, self.title_label)
        
        # PC ---------------------------------------------------------------------
        self.pc_menu = ctk.CTkLabel(self, text="")
        self.pc_menu.place(x=constants.WIDTH/2, y=constants.HEIGHT/2-50, anchor="center")
        
        self.pc_menu_animation = PC_MENUAnimation(self, self.pc_menu)
        
        
        # Dialogue ---------------------------------------------------------------
        self.dialogue_label = ctk.CTkTextbox(self,
                                        font=get_UPPERCASE(26), text_color="white",
                                        width=650,
                                        height=150,
                                        border_width=3, corner_radius=1, border_color="white",
                                        
                                        bg_color=constants.BACKGROUND_COLOR,
                                        fg_color=constants.BACKGROUND_COLOR,
                                        activate_scrollbars=False,
                                        wrap=WORD)
        self.dialogue_label.place(x=constants.WIDTH/2, y=constants.HEIGHT/2+180, anchor="center")
        
        self.dialogue_animation = DialogueAnimator(self, self.dialogue_label)
        
        # Buttons ----------------------------------------------------------------
        self.start_button = ctk.CTkButton(self, text="Jugar", font=get_TITLE(54),
                                        border_width=5, corner_radius=1, border_color="white",
                                        fg_color=constants.BACKGROUND_COLOR, text_color="white",
                                        hover_color=constants.COLOR_BLUE_HOVER)
        self.start_button.place(x=constants.WIDTH/2, y=constants.HEIGHT/2+300, anchor="center")
        
        self.option_button = ctk.CTkButton(self, text="Opciones", font=get_TITLE(40),
                                        border_width=5, corner_radius=1, border_color="white",
                                        fg_color=constants.BACKGROUND_COLOR, text_color="white",
                                        hover_color=constants.COLOR_YELLOW_HOVER)
        self.option_button.place(x=constants.WIDTH/2, y=constants.HEIGHT/2+370, anchor="center")
        
        self.exit_button = ctk.CTkButton(self, text="Salir", font=get_TITLE(40),
                                        border_width=5, corner_radius=1, border_color="white",
                                        fg_color=constants.BACKGROUND_COLOR, text_color="white",
                                        hover_color=constants.COLOR_RED_HOVER) 
        self.exit_button.place(x=constants.WIDTH/2, y=constants.HEIGHT/2+430, anchor="center")