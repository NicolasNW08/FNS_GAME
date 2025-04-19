from src.components.module.levels_menu.images import load_difficulty_images
from src.components.module.levels_menu.validation import validation_versus
from src.assets.font.fonts import get_LOWERCASE
from src.components.module.levels_menu.calculator_free import calculation_difficulty
from src.components.module.levels_menu.validation import validation_numbers, validation_free
from src.components.module.levels_menu.dialogues_randoms import random_dialog_add_players, random_dialog_difficulty

from src.assets.constant import constants
import customtkinter as ctk
import tkinter as tk
import os
from PIL import Image
import random

class Versus(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        self.controller = controller
        self.dificultad_images = load_difficulty_images()
        self.dialogue_animator = None
        
        
        # almacenamiento de los nombres de los jugadores
        self.players_values = {}
        
        # confirmadores de activar el juego
        self.players_ok = False
        self.difficulty_ok = True
        
        self.widgets()
        
    
    def back_to_main_levels(self):
        """Navigate back to the main levels selection screen"""
        self.reset()
        self.controller.back_to_main_levels()
    
    def start_game(self, min_val, max_val, attempts_val, players):
        
        if not validation_free(min_val, max_val, attempts_val, self.error_label):
            return
        
        dificultad = calculation_difficulty(min_val, max_val, attempts_val, self.error_label)
        print("-------------------------")
        print("TODO PERFECTO PARA JUGAR")
        print(f"Cantidad de jugadores: {len(players)} | Rondas: {len(players)}\n")
        for i, player in enumerate(players.values(), 1):  # Start indexing from 1
            print(f"jugador {i}: {player}")
        print(f"Minimo: {min_val} | Maximo: {max_val} | Intentos: {attempts_val} | Dificultad: {dificultad}")
        print("-------------------------\n")
        
        self.reset()

    def reset(self):
        self.players_values = {}
        
        self.players_list_textbox.configure(state="normal")
        self.players_list_textbox.delete("1.0", "end")
        self.players_list_textbox.configure(state="disabled")
        
        self.delete_players_options.configure(state="normal")
        self.delete_players_options.configure(values=list(self.players_values.keys()))
        self.delete_players_options.set("Eliminar jugador")
        self.delete_players_options.configure(state="readonly")
        
        self.player_add_entry.delete(0, "end")
        
        self.amount_players.configure(text=f"J 0")
        self.amount_players.configure(text_color=constants.ERROR_COLOR)
        
        self.button_game.configure(state="disabled")
        
        self.check_players.configure(text_color=constants.ERROR_COLOR)
        self.amount_players.configure(text_color=constants.ERROR_COLOR)
        self.check_difficulty.configure(text_color="green")
        
        self.error_general.configure(state="normal")
        self.error_general.delete(0, "end")
        self.error_general.configure(text_color=constants.ERROR_COLOR)
        self.error_general.configure(border_color=constants.ERROR_COLOR)
        self.error_general.insert("end", "Debe de haber MÍNIMO 2 JUGADORES")
        self.error_general.configure(state="disabled")
        
        image = self.dificultad_images.get(5, self.dificultad_images[1])
        self.dificultad_image.configure(image=image)
        
        self.error_label.configure(state="normal")
        self.error_label.delete("1.0", "end")
        self.error_label.configure(state="disabled")
        
        self.min_entry.delete(0, "end")
        self.max_entry.delete(0, "end")
        self.attempts_entry.delete(0, "end")
        
        self.min_entry.insert(0, "1")
        self.max_entry.insert(0, "3")
        self.attempts_entry.insert(0, "1")
        
        self.players_ok = False
        self.difficulty_ok = True

    def add_players(self):

        if self.player_add_entry.get() == "":
            return
        
        # comprobar si el jugador ya esta en la lista
        if self.player_add_entry.get() in self.players_values:
            return
        
        # self.players_values se usara para almacenar los nombres de los jugadores
        self.players_values[self.player_add_entry.get()] = self.player_add_entry.get()
        
        # random dialog
        self.error_label.configure(state="normal")
        self.error_label.configure(text_color="white")
        self.error_label.delete("1.0", "end")
        self.error_label.insert("end", random_dialog_add_players(self.player_add_entry.get()))
        self.error_label.configure(state="disabled")
        
        # add player to list
        self.players_list_textbox.configure(state="normal")
        self.players_list_textbox.insert("end", f"{self.player_add_entry.get()}\n")
        self.players_list_textbox.configure(state="disabled")
        self.player_add_entry.delete(0, "end")
        
        # update players list
        self.delete_players_options.configure(state="normal")
        self.delete_players_options.configure(values=list(self.players_values.keys()))
        self.delete_players_options.configure(state="readonly")
        
        self.amount_players.configure(text=f"J {len(self.players_values)}")
        
        if len(self.players_values) >= 2:
            self.button_game.configure(state="normal")
            self.check_players.configure(text_color="green")
            self.amount_players.configure(text_color="green")
            self.players_ok = True
        else:
            self.button_game.configure(state="disabled")
            self.check_players.configure(text_color=constants.ERROR_COLOR)
            self.amount_players.configure(text_color=constants.ERROR_COLOR)
            self.players_ok = False
        
        validation_versus(self.players_ok, self.difficulty_ok, self.button_game, self.error_general)

    def delete_players(self):
        
        if self.delete_players_options.get() == "" or self.delete_players_options.get() not in self.players_values:
            return
        if self.delete_players_options.get() == "Eliminar jugador":
            return
        
        selected_player = self.delete_players_options.get()
        
        if selected_player in self.players_values:
            del self.players_values[selected_player]
            self.players_list_textbox.configure(state="normal")
            self.players_list_textbox.delete(f"1.0", "end")
            for player in self.players_values:
                self.players_list_textbox.insert("end", f"{player}\n")
                
            self.players_list_textbox.configure(state="disabled")
            self.delete_players_options.configure(state="normal")
            self.delete_players_options.configure(values=list(self.players_values.keys()))
            self.delete_players_options.set("Eliminar jugador")
            self.delete_players_options.configure(state="readonly")
            
            self.amount_players.configure(text=f"J {len(self.players_values)}")
            
            
            if len(self.players_values) >= 2:
                self.players_ok = True
                self.check_players.configure(text_color="green")
                self.amount_players.configure(text_color="green")
            else:
                self.players_ok = False
                self.check_players.configure(text_color=constants.ERROR_COLOR)
                self.amount_players.configure(text_color=constants.ERROR_COLOR)
                
            
            validation_versus(self.players_ok, self.difficulty_ok, self.button_game, self.error_general)

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
                    image = ctk.CTkImage(light_image=image, dark_image=image, size=(128*1.1, 128*1.1))
                    self.dificultad_image.configure(image=image)
                    self.difficulty_ok = False
                    self.check_difficulty.configure(text_color=constants.ERROR_COLOR)
                    self.error_label.configure(text_color=constants.ERROR_COLOR)
                    validation_versus(self.players_ok, self.difficulty_ok, self.button_game, self.error_general)
                    
                    return
                
                self.error_label.configure(state="disabled")
                
                difficulty = calculation_difficulty(min_val, max_val, attempts, self.error_label)
                print(f"Dificultad calculada: {difficulty}")
                self.check_difficulty.configure(text_color="green")
                
                image = self.dificultad_images.get(difficulty, self.dificultad_images[1])
                self.dificultad_image.configure(image=image)
                self.difficulty_ok = True

                message = random_dialog_difficulty(difficulty)
                self.error_label.configure(state="normal")
                self.error_label.delete("1.0", "end")
                self.error_label.insert("1.0", f"({difficulty}): {message}")
                self.error_label.configure(state="disabled")
                self.error_label.configure(text_color="white") 
                validation_versus(self.players_ok, self.difficulty_ok, self.button_game, self.error_general)
                
            except ValueError as e:
                print(f"Error en update_difficulty_image: {e}")

        # Frame principal
        frame = ctk.CTkFrame(self, fg_color=constants.BACKGROUND_COLOR, 
                            border_color="white", border_width=4,
                            width=655, height=850, corner_radius=0)
        frame.place(x=constants.WIDTH/2, y=constants.HEIGHT/2, anchor="center")
        
        
        # Título
        title_label = ctk.CTkButton(frame, text="VERSUS", 
                                    font=get_LOWERCASE(38), text_color="white",
                                    hover=False, fg_color=constants.BACKGROUND_COLOR,
                                    border_color="white", border_width=2,
                                    width=250, height=60)
        title_label.place(x=655/2, y=constants.HEIGHT/2-423, anchor="center")
        
        # --- add players ---
        
        # players label
        players_label = ctk.CTkLabel(frame, text="JUGADORES", 
                                    corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=40, 
                                    font=get_LOWERCASE(26), text_color="white")
        players_label.place(x=655/2-227, y=constants.HEIGHT/2-380, anchor="n")
        
        #players list
        self.players_list_textbox = ctk.CTkTextbox(frame, 
                                            font=get_LOWERCASE(22), text_color="white",
                                            corner_radius=10, fg_color=constants.BG_GRAY_2, 
                                            width=175, height=280,  wrap="word"
                                            
        )
        self.players_list_textbox.place(x=655/2-315, y=constants.HEIGHT/2-336, anchor="nw")
        
        self.player_add_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(24), text_color="white", 
                                width=443, height=60, corner_radius=10, border_width=2, 
                                border_color="white", fg_color=constants.BG_GRAY_1,
                                
                                placeholder_text="NOMBRE DEL JUGADOR")
        self.player_add_entry.place(x=655/2-131, y=constants.HEIGHT/2-330, anchor="nw")
        
        player_add_button = ctk.CTkButton(frame, text="AGREGAR JUGADOR", font=get_LOWERCASE(28), text_color="white",
                                        fg_color=constants.COLOR_BLUE, hover_color=constants.COLOR_BLUE_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=self.add_players)
        player_add_button.place(x=655/2-130, y=constants.HEIGHT/2-260, anchor="nw")
        
        # delete players options
        self.delete_players_options = ctk.CTkComboBox(frame, font=get_LOWERCASE(30), text_color="white", 
                                                        corner_radius=0, fg_color=constants.BG_GRAY_1, 
                                                        width=443, height=60, 
                                                        border_width=2, border_color="white",
                                                        
                                                        state="readonly",
                                                        command=None,
                                                        
                                                        button_color=constants.BG_GRAY_3,
                                                        button_hover_color=constants.BG_GRAY_2,
                                                        dropdown_fg_color=constants.BG_GRAY_1,
                                                        dropdown_hover_color=constants.BG_GRAY_1,
                                                        dropdown_text_color="white",
                                                        dropdown_font=get_LOWERCASE(24),
                                                        justify="center")
        self.delete_players_options.set("Eliminar jugador")
        self.delete_players_options.place(x=655/2-130, y=constants.HEIGHT/2-180, anchor="nw")
        
        # delete players button
        self.delete_players_button = ctk.CTkButton(frame, text="ELIMINAR JUGADOR", font=get_LOWERCASE(28), text_color="white",
                                        fg_color=constants.COLOR_BLUE, hover_color=constants.COLOR_BLUE_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=self.delete_players)
        self.delete_players_button.place(x=655/2-130, y=constants.HEIGHT/2-110, anchor="nw")
        
        # amount players
        self.amount_players = ctk.CTkButton(frame, text="J 0", font=get_LOWERCASE(34), text_color=constants.ERROR_COLOR, width=100, height=50,
                                            border_width=3, border_color="white", corner_radius=0, fg_color=constants.BG_GRAY_2,
                                            hover=False)
        self.amount_players.place(x=655/2-131, y=constants.HEIGHT/2-45, anchor="nw")
        
        self.check_players = ctk.CTkButton(frame, text="JUGADORES", font=get_LOWERCASE(28), text_color=constants.ERROR_COLOR, 
                                            width=100, height=50,
                                            border_width=3, border_color="white", 
                                            corner_radius=0, fg_color=constants.BG_GRAY_2,
                                            hover=False)
        self.check_players.place(x=655/2-27, y=constants.HEIGHT/2-45, anchor="nw")
        
        self.check_difficulty = ctk.CTkButton(frame, text="DIFICULTAD", font=get_LOWERCASE(28), 
                                            text_color="green", 
                                            width=100, height=50,
                                            border_width=3, border_color="white", 
                                            corner_radius=0, fg_color=constants.BG_GRAY_2,
                                            hover=False)
        self.check_difficulty.place(x=655/2+140, y=constants.HEIGHT/2-45, anchor="nw")
        
        self.error_general = ctk.CTkEntry(frame, font=get_LOWERCASE(26), text_color=constants.ERROR_COLOR, 
                                            width=550, height=62,
                                            border_width=3, border_color=constants.ERROR_COLOR, 
                                            corner_radius=0, fg_color=constants.BG_GRAY_2,
                                            justify="center")
        self.error_general.place(x=655/2, y=constants.HEIGHT/2+220, anchor="n")
        self.error_general.insert(0, "Debe de haber MÍNIMO 2 JUGADORES")
        self.error_general.configure(state="disabled")
        
        #--- PRE LOADED ---
        
        
        # error difficulty
        self.error_label = ctk.CTkTextbox(frame, font=get_LOWERCASE(16), 
                                        text_color=constants.ERROR_COLOR, corner_radius=10, fg_color=constants.BG_GRAY_2, 
                                        width=600, height=50, state="disabled", 
                                        activate_scrollbars=False, wrap="word"
                                        )
        self.error_label.place(x=655/2, y=constants.HEIGHT/2+165, anchor="n")
        
        
        self.dificultad_image = ctk.CTkLabel(frame, text="", font=get_LOWERCASE(24), text_color="white",
                                    width=128, height=128)
        self.dificultad_image.place(x=655/2-227, y=constants.HEIGHT/2+14, anchor="n")
        
        
        difficulty_label = ctk.CTkLabel(frame, text="DIFICULTAD", font=get_LOWERCASE(24), text_color="white",
                                        corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50)
        difficulty_label.place(x=655/2-227, y=constants.HEIGHT/2-45, anchor="n")
        
        
        # min - max - attempts labels
        min_label = ctk.CTkLabel(frame, text="MÍNIMO", 
                                corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                font=get_LOWERCASE(24), text_color="white")
        min_label.place(x=655/2-140+10+15, y=constants.HEIGHT/2+35, anchor="nw")
        
        max_label = ctk.CTkLabel(frame, text="MÁXIMO", 
                                corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                font=get_LOWERCASE(24), text_color="white")
        max_label.place(x=655/2-140+140+10+15, y=constants.HEIGHT/2+35, anchor="nw")
        
        attempts_label = ctk.CTkLabel(frame, text="INTENTOS", 
                                    corner_radius=10, fg_color=constants.BG_GRAY_2, width=100, height=50, 
                                    font=get_LOWERCASE(24), text_color="white")
        attempts_label.place(x=655/2-140+280+10+15, y=constants.HEIGHT/2+35, anchor="nw")
        
        # min - max - attempts entrys
        self.min_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(24), text_color="white", 
                                width=100, height=50, corner_radius=10, border_width=2, 
                                border_color="white", fg_color=constants.BG_GRAY_1,
                                validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.min_entry.place(x=655/2-140+3+10+15, y=constants.HEIGHT/2+105, anchor="nw")
        self.min_entry.insert(0, "1")
        
        self.max_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(24), text_color="white", 
                                width=100, height=50, corner_radius=10, border_width=2, 
                                border_color="white", fg_color=constants.BG_GRAY_1,
                                validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.max_entry.place(x=655/2-140+140+3+10+15, y=constants.HEIGHT/2+105, anchor="nw")
        self.max_entry.insert(0, "3")
        
        self.attempts_entry = ctk.CTkEntry(frame, font=get_LOWERCASE(24), text_color="white", 
                                    width=100, height=50, corner_radius=10, border_width=2, 
                                    border_color="white", fg_color=constants.BG_GRAY_1,
                                    validate="key", validatecommand=(self.register(validation_numbers), "%P"))
        self.attempts_entry.place(x=655/2-140+280+13+10+15, y=constants.HEIGHT/2+105, anchor="nw")
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
        
        # button reset
        self.button_rese = ctk.CTkButton(frame, text="RESETEAR", font=get_LOWERCASE(32), text_color="white",
                                        fg_color=constants.COLOR_RED, hover_color=constants.COLOR_RED_HOVER, 
                                        width=170, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.reset())
        self.button_rese.place(x=655/2-130, y=constants.HEIGHT/2+361, anchor="se")
        
        #button game
        self.button_game = ctk.CTkButton(frame, text="JUGAR", font=get_LOWERCASE(68), text_color="white", 
                                        fg_color=constants.COLOR_GREEN, hover_color=constants.COLOR_GREEN_HOVER, 
                                        state="disabled",
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.start_game(min_val=int(self.min_entry.get()), 
                                                                    max_val=int(self.max_entry.get()), 
                                                                    attempts_val=int(self.attempts_entry.get()), 
                                                                    players=self.players_values))
        self.button_game.place(x=655/2+315, y=constants.HEIGHT/2+361, anchor="se")
        
        # button back
        self.button_back = ctk.CTkButton(frame, text="VOLVER", font=get_LOWERCASE(52), text_color="white", 
                                        fg_color=constants.COLOR_YELLOW, hover_color=constants.COLOR_YELLOW_HOVER, 
                                        width=200, height=50, corner_radius=1, border_width=4, border_color="white",
                                        command=lambda: self.back_to_main_levels())
        self.button_back.place(x=655/2+90, y=constants.HEIGHT/2+360, anchor="se")