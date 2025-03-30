import tkinter as tk
from PIL import Image
import assets.constant.constants as constants
from customtkinter import CTkImage

class BGAnimation:
    def __init__(self, parent, label):
        self.parent = parent
        self.bg_label = label
        self.frames = []  # Lista para almacenar los frames
        self.index = 0  # Índice del frame actual

        # Cargar los 5 frames
        for i in range(1, 6):
            img = Image.open(f"assets/img/backgrounds/background{i}.png")
            img = img.resize((constants.WIDTH, constants.HEIGHT))  # Ajustar tamaño
            self.frames.append(CTkImage(light_image=img, size=(constants.WIDTH, constants.HEIGHT)))  # Convertir a formato de CTk

        # Iniciar la animación
        self.animate()

    def animate(self):
        # Cambiar la imagen del fondo
        self.bg_label.configure(image=self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)  # Ir al siguiente frame en loop
        self.parent.after(500, self.animate)  # Volver a llamar en 500ms