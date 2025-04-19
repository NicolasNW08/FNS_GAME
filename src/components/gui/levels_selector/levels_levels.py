import json
import os
from PIL import Image
import customtkinter as ctk
from src.components.module.levels_menu.images import load_difficulty_images
from src.assets.font.fonts import *
from src.assets.constant import constants

class Levels(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        self.level_data = self.load_levels()  # Cargar niveles desde JSON
        self.difficulty_icons = load_difficulty_images()
        
        self.widgets()
        
    def load_levels(self):
        """ Carga los niveles desde el archivo JSON. """
        try:
            with open("src/components/config/levels_configuration/levels.json", "r") as file:
                return json.load(file)  # Retorna lista de niveles
        except FileNotFoundError:
            print("Error: Archivo levels.json no encontrado.")
            return []  # Retorna lista vacía si hay error
        
    def create_level_buttons(self):
        """ Genera los botones de nivel dinámicamente en 2 columnas. """
        for idx, level in enumerate(self.level_data):
            level_num = level["level"]
            level_name = level["name"]
            level_dificulty = level["dificulty"]
            level_min_val = level["min"]
            level_max_val = level["max"]
            level_attempts = level["attempts"]
            level_finalized = level["finalized"]
            
            image = self.difficulty_icons.get(level_dificulty)

            btn = ctk.CTkButton(self.scrollable_frame,
                                text=f"Nivel N°{level_num}: {level_name}\nDificultad: {level_dificulty}\nRango: {level_min_val} - {level_max_val}\nIntentos: {level_attempts}",
                                font=get_LOWERCASE(28),
                                text_color="white",
                                fg_color="green" if level_finalized else "gray",
                                border_color="white", border_width=2,
                                width=280, height=280,
                                image=image, compound="top",
                                state="normal" if level_finalized else "disabled",
                                command=lambda lv=level: self.start_level(lv))

            # Distribuir en dos columnas
            row = idx // 2  # Calcula la fila
            column = idx % 2  # Alterna entre 0 y 1

            btn.grid(row=row, column=column, padx=18, pady=20, sticky="ew")

    def start_level(self, level):
        """ Inicia el nivel con los parámetros del JSON. """
        print(f"Iniciando Nivel N°{level['level']}: {level['name']}\nDificultad: {level['dificulty']}\nRango: {level['min']} - {level['max']}\nIntentos: {level['attempts']}")
        # Aquí puedes agregar la lógica para cambiar de pantalla al juego
    
    def back_to_main_levels(self):
        """Navigate back to the main levels selection screen"""
        self.controller.back_to_main_levels()
    
    def widgets(self):
        # Frame principal
        frame = ctk.CTkFrame(self, fg_color=constants.BACKGROUND_COLOR, 
                             border_color="white", border_width=4,
                             width=constants.WIDTH/2+280, height=constants.HEIGHT/2+400,
                             corner_radius=0)
        frame.place(x=constants.WIDTH/2, y=constants.HEIGHT/2, anchor="center")
        
        # Título
        title_label = ctk.CTkButton(frame, text="SELECCIONÁ NIVEL", 
                                    font=get_LOWERCASE(42), text_color="white",
                                    hover=False, fg_color=constants.BACKGROUND_COLOR,
                                    border_color="white", border_width=2,
                                    width=250, height=60)
        title_label.place(x=655/2, y=constants.HEIGHT/2-423, anchor="center")
        
        # ScrollFrame para los niveles
        self.scrollable_frame = ctk.CTkScrollableFrame(frame, fg_color=constants.BACKGROUND_COLOR, 
                                                    border_color="white", border_width=4, 
                                                    width=630, height=660,
                                                    corner_radius=0)
        self.scrollable_frame.place(x=655/2, y=constants.HEIGHT/2-370, anchor="n")
        
        # button back
        self.button_back = ctk.CTkButton(frame, text="VOLVER", font=get_LOWERCASE(54), text_color="white", 
                                        fg_color=constants.COLOR_YELLOW, hover_color=constants.COLOR_YELLOW_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.back_to_main_levels())
        self.button_back.place(x=655/2, y=constants.HEIGHT/2+315, anchor="n")

        # Crear los botones de niveles
        self.create_level_buttons()