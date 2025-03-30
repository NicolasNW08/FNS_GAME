import tkinter as tk
from PIL import Image
import assets.constant.constants as constants
from customtkinter import CTkImage
import random

class PC_MENUAnimation:
    def __init__(self, parent, label):
        self.parent = parent
        self.label = label
        self.frames = []  # Lista para almacenar los frames
        self.last_two_indexes = [-1, -1]  # Para evitar repetir las dos últimas imágenes

        # Cargar los 6 frames
        for i in range(1, 7):
            img = Image.open(f"assets/img/PC/pc{i}.png")
            img = img.resize((175, 163))  # Ajustar tamaño
            self.frames.append(CTkImage(light_image=img, size=(175*3.2, 163*3.2)))   # Convertir a formato de CTk

        # Iniciar la animación
        self.animate()

    def animate(self):
        # Elegir una imagen aleatoria que NO sea ninguna de las dos últimas
        available_indexes = [i for i in range(len(self.frames)) if i not in self.last_two_indexes]
        new_index = random.choice(available_indexes)  # Elegir un índice válido

        # Actualizar la imagen en el label
        self.label.configure(image=self.frames[new_index], text="")    

        # Actualizar historial de imágenes (mantener solo las dos últimas)
        self.last_two_indexes.append(new_index)
        if len(self.last_two_indexes) > 2:
            self.last_two_indexes.pop(0)  # Elimina el más antiguo

        # Esperar un tiempo aleatorio antes del siguiente cambio
        self.parent.after(random.randint(100, 300), self.animate)
