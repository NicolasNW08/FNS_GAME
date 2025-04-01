from tkinter import ttk, WORD
import customtkinter as ctk
from PIL import Image, ImageTk
from assets.animation.dialogue_animation import DialogueAnimator
import assets.constant.constants as constants
from assets.font.fonts import *

from assets.animation.pc_menu_animation import PC_MENUAnimation
from assets.animation.title_animation import TITLEAnimation
from assets.animation.bg_animation import BGAnimation

from language.es_ES import *


class Menu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack()
        self.place(x=0,y=0, relwidth=1, relheight=1)
        self.controller = controller
        self.configure(bg_color=constants.BACKGROUND_COLOR, 
                        fg_color=constants.BACKGROUND_COLOR,
                        border_color="white", border_width=2)

        self.widgets()

    
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
                                        hover_color=constants.COLOR_BLUE_HOVER,
                                        command=lambda: self.controller.show_frame("Levels"))
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