import customtkinter as ctk
from PIL import Image
import os

def load_difficulty_images():
    """ Carga imágenes de dificultad (d1.png a d7.png) en un diccionario. """
    images = {}
    for i in range(1, 8):
        path = f"src/assets/img/levels faces/d{i}.png"
        if os.path.exists(path):
            image = Image.open(path).resize((128, 128))
            images[i] = ctk.CTkImage(light_image=image, dark_image=image, size=(128*1.4, 128*1.4))
        else:
            print(f"Advertencia: imagen de dificultad no encontrada: {path}")
            images[i] = None
    return images