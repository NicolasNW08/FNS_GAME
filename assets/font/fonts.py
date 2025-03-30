import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageFont
import customtkinter as ctk
from customtkinter import CTkFont

# Rutas de las fuentes
LOWERCASE_PATH = "assets/font/upheavtt.ttf"
UPPERCASE_PATH = "assets/font/PixelifySans-VariableFont_wght.ttf"
ALTERNATIVE_PATH = "assets/font/niideache.ttf"

# Registrar las fuentes en Tkinter
def register_font(font_path):
    try:
        font = ImageFont.truetype(font_path, size=10)  # Cargar fuente con PIL
        return font.getname()[0]  # Obtener el nombre interno de la fuente
    except Exception as e:
        print(f"Error al cargar la fuente {font_path}: {e}")
        return "Impact"  # Fuente por defecto si falla

LOWERCASE = register_font(LOWERCASE_PATH)
UPPERCASE = register_font(UPPERCASE_PATH)
ALTERNATIVE = register_font(ALTERNATIVE_PATH)

# Funciones para obtener fuentes con diferentes tamaños
def get_LOWERCASE(size):
    return ctk.CTkFont(family=LOWERCASE, size=size)

def get_UPPERCASE(size):
    return ctk.CTkFont(family=UPPERCASE, size=size, weight="bold")

def get_ALTERNATIVE(size):
    return ctk.CTkFont(family=ALTERNATIVE, size=size)

# TITULOS

def get_TITLE(size):
    return ctk.CTkFont(family=ALTERNATIVE, size=size, weight="bold")