import random
import tkinter as tk
from src.language.es_ES import PRESENTATION

class DialogueAnimator:
    def __init__(self, parent, dialogue_widget):
        self.parent = parent
        self.dialogue_widget = dialogue_widget
        self.text = ""
        self.index = 0
        self.typing_speed = 50  # Velocidad normal de escritura en ms
        self.newline_delay = 1000  # Retraso extra en saltos de línea
        self.wait_time = 3500  # Tiempo de espera antes de cambiar de diálogo
        self.last_texts = []  # Guardar los últimos dos diálogos

        self.start_typing()

    def get_new_dialogue(self):
        """Selecciona un diálogo evitando los dos últimos utilizados."""
        available_texts = [t for t in PRESENTATION if t not in self.last_texts]
        new_text = random.choice(available_texts)

        # Actualizar los diálogos anteriores
        self.last_texts.append(new_text)
        if len(self.last_texts) > 2:
            self.last_texts.pop(0)  # Mantener solo los últimos dos

        return new_text

    def start_typing(self):
        """Inicia la animación de escritura con un nuevo diálogo."""
        self.text = self.get_new_dialogue()
        self.index = 0
        self.dialogue_widget.configure(state=tk.NORMAL)
        self.dialogue_widget.delete("1.0", tk.END)
        self.dialogue_widget.configure(state=tk.DISABLED)

        # Iniciar la animación de escritura
        self.animate_typing()

    def animate_typing(self):
        """Escribe letra por letra y aplica un retraso extra en saltos de línea."""
        if self.index < len(self.text):
            self.dialogue_widget.configure(state=tk.NORMAL)
            self.dialogue_widget.insert(tk.END, self.text[self.index])
            self.dialogue_widget.configure(state=tk.DISABLED)

            delay = self.newline_delay if self.text[self.index] == "\n" else self.typing_speed
            self.index += 1
            self.parent.after(delay, self.animate_typing)
        else:
            # Esperar un poco y cambiar al siguiente diálogo
            self.parent.after(self.wait_time, self.start_typing)