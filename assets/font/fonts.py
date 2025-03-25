import tkinter as tk
from tkinter import *
from tkinter import font as tkfont


LOWERCASE = "assets/font/joystix monospace.otf"
UPPERCASE = "assets/font/PixelifySans-VariableFont_wght.ttf"
ALTERNATIVE = "assets/font/niideache.ttf"

def get_LOWERCASE(size):
    return tkfont.Font(family=LOWERCASE, size=size, weight="normal")

def get_UPPERCASE(size):
    return tkfont.Font(family=UPPERCASE, size=size, weight="normal")

def get_ALTERNATIVE(size):
    return tkfont.Font(family=ALTERNATIVE, size=size, weight="normal")