import tkinter as tk
from PIL import Image
from src.core.constant import constants
from customtkinter import CTkImage

class BGAnimation:
    def __init__(self, parent, label):
        self.parent = parent
        self.bg_label = label
        self.frames = []
        self.index = 0
        self.running = False
        self.after_id = None

        for i in range(1, 6):
            img = Image.open(f"src/assets/img/backgrounds/background{i}.png")
            img = img.resize((constants.WIDTH, constants.HEIGHT))
            self.frames.append(CTkImage(light_image=img, size=(constants.WIDTH, constants.HEIGHT)))

        self.resume()

    def animate(self):
        if not self.running:
            return
        self.bg_label.configure(image=self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)
        self.after_id = self.parent.after(500, self.animate)

    def pause(self):
        self.running = False
        if self.after_id:
            self.parent.after_cancel(self.after_id)
            self.after_id = None

    def resume(self):
        if not self.running:
            self.running = True
            self.animate()
