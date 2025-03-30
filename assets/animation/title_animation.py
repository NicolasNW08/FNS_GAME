import tkinter as tk
from PIL import Image
import assets.constant.constants as constants
from customtkinter import CTkImage

class TITLEAnimation:
    def __init__(self, parent, label):
        self.parent = parent
        self.title = label
        self.frames = []  # Lista para almacenar los frames
        self.index = 0  # Índice del frame actual

        # Cargar los 3 frames
        for i in range(1, 4):
            img = Image.open(f"assets/img/securities/title{i}.png")
            img = img.resize((710, 120))  # Ajustar tamaño
            self.frames.append(CTkImage(light_image=img, size=(710, 120)))  # Convertir a formato de CTk

        # Iniciar la animación
        self.animate()

    def animate(self):
        # Cambiar la imagen del fondo
        self.title.configure(image=self.frames[self.index], text="")    
        self.index = (self.index + 1) % len(self.frames)  # Ir al siguiente frame en loop
        self.parent.after(300, self.animate)  # Volver a llamar en 500ms