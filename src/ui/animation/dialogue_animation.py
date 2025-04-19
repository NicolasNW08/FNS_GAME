import random
import tkinter as tk
from src.core.language.es_ES import PRESENTATION

class DialogueAnimator:
    def __init__(self, parent, dialogue_widget):
        self.parent = parent
        self.dialogue_widget = dialogue_widget
        self.text = ""
        self.index = 0
        self.typing_speed = 50
        self.newline_delay = 1000
        self.wait_time = 3500
        self.last_texts = []

        self.running = False
        self.after_id = None

        self.resume()  # Comienza automáticamente

    def get_new_dialogue(self):
        available_texts = [t for t in PRESENTATION if t not in self.last_texts]
        new_text = random.choice(available_texts)
        self.last_texts.append(new_text)
        if len(self.last_texts) > 2:
            self.last_texts.pop(0)
        return new_text

    def start_typing(self):
        self.text = self.get_new_dialogue()
        self.index = 0
        self.dialogue_widget.configure(state=tk.NORMAL)
        self.dialogue_widget.delete("1.0", tk.END)
        self.dialogue_widget.configure(state=tk.DISABLED)

        self.animate_typing()

    def animate_typing(self):
        if not self.running:
            return

        if self.index < len(self.text):
            self.dialogue_widget.configure(state=tk.NORMAL)
            self.dialogue_widget.insert(tk.END, self.text[self.index])
            self.dialogue_widget.configure(state=tk.DISABLED)

            delay = self.newline_delay if self.text[self.index] == "\n" else self.typing_speed
            self.index += 1
            self.after_id = self.parent.after(delay, self.animate_typing)
        else:
            self.after_id = self.parent.after(self.wait_time, self.start_typing)

    def pause(self):
        self.running = False
        if self.after_id:
            self.parent.after_cancel(self.after_id)
            self.after_id = None

    def resume(self):
        if not self.running:
            self.running = True
            self.start_typing()
