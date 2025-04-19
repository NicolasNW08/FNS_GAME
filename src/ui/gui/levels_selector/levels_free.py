from PIL import Image
from src.assets.font.fonts import *

from src.core.module.levels_menu.dialogues_randoms import random_dialog
from src.core.module.levels_menu.validation import validation_numbers, validation_free
from src.core.module.levels_menu.images import load_difficulty_images
from src.core.module.levels_menu.calculator_free import calculation_difficulty

from src.core.constant import constants
import customtkinter as ctk

class Free(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        self.controller = controller
        self.dificultad_images = load_difficulty_images()
        self.dialogue_animator = None
        self.widgets()
        
    def back_to_main_levels(self):
        """Navigate back to the main levels selection screen"""
        self.reset()
        self.controller.back_to_main_levels()
    
    def start_game(self, min_val, max_val, attempts_val):
        
        if not validation_free(min_val, max_val, attempts_val, self.error_label):
            return
        
        difficulty = calculation_difficulty(min_val, max_val, attempts_val, self.error_label)
        print("-------------------------")
        print("TODO PERFECTO PARA JUGAR")
        print(f"Minimo: {min_val} | Maximo: {max_val} | Intentos: {attempts_val} | Dificultad: {difficulty}")
        print("-------------------------\n")
        
        self.reset()
    
    def reset(self):
        
        self.min_entry.delete(0, "end")
        self.max_entry.delete(0, "end")
        self.attempts_entry.delete(0, "end")
        
        
        self.error_label.configure(state="normal")
        self.error_label.delete("1.0", "end")
        self.error_label.configure(state="disabled")
        
        
        image = self.dificultad_images.get(5, self.dificultad_images[1])
        self.dificultad_image.configure(image=image)
        
        self.button_game.configure(state="disabled")
    
    def widgets(self):


        def update_difficulty_image(event=None):
            try:
                # Leer valores como texto
                min_text = self.min_entry.get()
                max_text = self.max_entry.get()
                attempts_text = self.attempts_entry.get()

                # Si alguno está vacío, no actualizamos nada todavía
                if not min_text or not max_text or not attempts_text:
                    self.button_game.configure(state="disabled")

                    return  # Simplemente esperamos a que se complete

                # Convertimos a int
                min_val = int(min_text)
                max_val = int(max_text)
                attempts = int(attempts_text)
                

                if not validation_free(min_val, max_val, attempts, self.error_label):
                    self.error_label.configure(state="disabled")

                    path = "src/assets/img/error.png"
                    image = Image.open(path).resize((128, 128))
                    image = ctk.CTkImage(light_image=image, dark_image=image, size=(128*1.4, 128*1.4))
                    self.dificultad_image.configure(image=image)
                    self.button_game.configure(state="disabled", fg_color=constants.ERROR_COLOR)
                    self.error_label.configure(text_color=constants.ERROR_COLOR)
                    
                    return
                
                self.error_label.configure(state="disabled")
                
                difficulty = calculation_difficulty(min_val, max_val, attempts, self.error_label)
                print(f"Dificultad calculada: {difficulty}")
                
                image = self.dificultad_images.get(difficulty, self.dificultad_images[1])
                self.dificultad_image.configure(image=image)
                self.button_game.configure(state="normal")

                message = random_dialog(difficulty)
                self.error_label.configure(state="normal")
                self.error_label.delete("1.0", "end")
                self.error_label.insert("1.0", f"({difficulty}): {message}")
                self.error_label.configure(state="disabled")
                self.error_label.configure(text_color="white")
                
                
                
                

            except ValueError as e:
                print(f"Error en update_difficulty_image: {e}")

        # Frame principal
        frame = ctk.CTkFrame(self, fg_color=constants.BACKGROUND_COLOR, 
                            border_color="white", border_width=4,
                            width=655, height=850, corner_radius=0)
        frame.place(x=constants.WIDTH/2, y=constants.HEIGHT/2, anchor="center")
        
        # Errors labels
        self.error_label = ctk.CTkTextbox(frame, font=get_LOWERCASE(22), 
                                        text_color=constants.ERROR_COLOR, corner_radius=10, fg_color=constants.BG_GRAY_2, 
                                        width=600, height=50, state="disabled", 
                                        activate_scrollbars=False, wrap="word"
                                        )
        self.error_label.place(x=655/2, y=constants.HEIGHT/2+165, anchor="n")
        
        
        self.dificultad_image = ctk.CTkLabel(frame, text="", font=get_LOWERCASE(38), text_color="white",
                                    width=128, height=128)
        self.dificultad_image.place(x=655/2, y=constants.HEIGHT/2-20, anchor="n")
        
        
        difficulty_label = ctk.CTkLabel(frame, text="DIFICULTAD", font=get_LOWERCASE(38), text_color="white",
                                        corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50)
        difficulty_label.place(x=655/2, y=constants.HEIGHT/2-90, anchor="n")
        
        # Título
        title_label = ctk.CTkButton(frame, text="MODO LIBRE", 
                                    font=get_LOWERCASE(42), text_color="white",
                                    hover=False, fg_color=constants.BACKGROUND_COLOR,
                                    border_color="white", border_width=2,
                                    width=250, height=60)
        title_label.place(x=655/2, y=constants.HEIGHT/2-423, anchor="center")
        
        
        # min - max - attempts labels
        min_label = ctk.CTkLabel(frame, text="MÍNIMO", 
                                corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                font=get_LOWERCASE(38), text_color="white")
        min_label.place(x=655/2-100, y=constants.HEIGHT/2-370, anchor="n")
        
        max_label = ctk.CTkLabel(frame, text="MÁXIMO", 
                                corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                font=get_LOWERCASE(38), text_color="white")
        max_label.place(x=655/2+100, y=constants.HEIGHT/2-370, anchor="n")
        
        attempts_label = ctk.CTkLabel(frame, text="INTENTOS", 
                                    corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                    font=get_LOWERCASE(38), text_color="white")
        attempts_label.place(x=655/2, y=constants.HEIGHT/2-230, anchor="n")
        
        # min - max - attempts entrys
        self.min_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(38), text_color="white", 
                                width=100, height=50, corner_radius=10, border_width=2, 
                                border_color="white", fg_color=constants.BG_GRAY_1,
                                validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.min_entry.place(x=655/2-100, y=constants.HEIGHT/2-300, anchor="n")
        self.min_entry.insert(0, "1")
        
        self.max_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(38), text_color="white", 
                                width=100, height=50, corner_radius=10, border_width=2, 
                                border_color="white", fg_color=constants.BG_GRAY_1,
                                validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.max_entry.place(x=655/2+100, y=constants.HEIGHT/2-300, anchor="n")
        self.max_entry.insert(0, "3")
        
        self.attempts_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(38), text_color="white", 
                                    width=100, height=50, corner_radius=10, border_width=2, 
                                    border_color="white", fg_color=constants.BG_GRAY_1,
                                    validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.attempts_entry.place(x=655/2, y=constants.HEIGHT/2-160, anchor="n")
        self.attempts_entry.insert(0, "1")
        
        # Bind the update function to all entry widgets
        self.min_entry.bind("<KeyRelease>", update_difficulty_image)
        self.max_entry.bind("<KeyRelease>", update_difficulty_image)
        self.attempts_entry.bind("<KeyRelease>", update_difficulty_image)
        
        # Now that all widgets exist and are properly configured, set the initial image
        initial_image = self.dificultad_images[calculation_difficulty(int(self.min_entry.get()), int(self.max_entry.get()), int(self.attempts_entry.get()), self.error_label)]
        self.dificultad_image.configure(image=initial_image)
        
        # bind min - max - attempts
        self.min_entry.bind("<KeyRelease>", update_difficulty_image)
        self.max_entry.bind("<KeyRelease>", update_difficulty_image)
        self.attempts_entry.bind("<KeyRelease>", update_difficulty_image)
        
        # Now that all widgets exist, set the initial image
        initial_image = self.dificultad_images[calculation_difficulty(int(self.min_entry.get()), int(self.max_entry.get()), int(self.attempts_entry.get()), self.error_label)]
        self.dificultad_image.configure(image=initial_image)
        
        # button game
        self.button_game = ctk.CTkButton(frame, text="JUGAR", font=get_LOWERCASE(46), text_color="white", 
                                        fg_color=constants.COLOR_GREEN, hover_color=constants.COLOR_GREEN_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.start_game(min_val=int(self.min_entry.get()), 
                                                                     max_val=int(self.max_entry.get()), 
                                                                     attempts_val=int(self.attempts_entry.get())))
        self.button_game.place(x=655/2, y=constants.HEIGHT/2+230, anchor="n")
        
        # button back
        self.button_back = ctk.CTkButton(frame, text="VOLVER", font=get_LOWERCASE(46), text_color="white", 
                                        fg_color=constants.COLOR_YELLOW, hover_color=constants.COLOR_YELLOW_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.back_to_main_levels())
        self.button_back.place(x=655/2, y=constants.HEIGHT/2+300, anchor="n")
        
