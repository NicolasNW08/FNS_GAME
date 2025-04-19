import tkinter as tk

def validation_free(min_val, max_val, attempts, text_label):
    try:
        def mostrar(msg):
            text_label.configure(state="normal")
            text_label.delete("1.0", tk.END)
            text_label.insert(tk.END, msg)
            text_label.configure(state="disabled")

        if min_val < 0 or max_val < 0 or attempts <= 0:
            mostrar("valores negativos o intentos cero")
            return False

        if min_val >= max_val:
            mostrar("minimo mayor o igual al maximo")
            return False

        if (max_val - min_val) <= 1:
            mostrar("no hay suficientes números en el rango")
            return False

        if (max_val - min_val) < 2:
            mostrar("rango sin números jugables")
            return False

        if attempts > (max_val - min_val - 1):
            mostrar("demasiados intentos para tan pocos números")
            return False

        
        text_label.configure(state="normal")
        text_label.delete("1.0", tk.END)
        text_label.insert(tk.END, "")
        text_label.configure(state="disabled")

        return True

    except Exception as e:
        text_label.configure(state="normal")
        text_label.delete("1.0", tk.END)
        text_label.insert(tk.END, f"error en validation_free: {e}")
        text_label.configure(state="disabled")

        return False


def validation_numbers(valor):
    return valor.isdigit() or valor == ""
    
from src.core.constant import constants

def validation_versus(players, difficulty, button_start_game, error_label):
    try:
        if players is False:
            button_start_game.configure(state="disabled")
            error_label.configure(state="normal")
            error_label.configure(text_color=constants.ERROR_COLOR)
            error_label.delete(0, tk.END)
            error_label.insert(tk.END, "Debe de haber MÍNIMO 2 JUGADORES")
            error_label.configure(state="disabled")
            error_label.configure(border_color=constants.ERROR_COLOR)
            print ("jugadores faltantes")
            return

        if difficulty is False:
            button_start_game.configure(state="disabled")
            error_label.configure(state="normal")
            error_label.configure(text_color=constants.ERROR_COLOR)
            error_label.delete(0, tk.END)
            error_label.insert(tk.END, "Parametros de Dificultad Erroneos")
            error_label.configure(state="disabled")
            error_label.configure(border_color=constants.ERROR_COLOR)
            print("dificultad faltante")
            return

        button_start_game.configure(state="normal")
        error_label.configure(text_color="green")
        error_label.configure(state="normal")
        error_label.delete(0, tk.END)
        error_label.insert(tk.END, "TODO PERFECTO PARA JUGAR")
        error_label.configure(border_color="green")
        error_label.configure(state="disabled")
        
        print("todo ok")
        return
    except Exception as e:
        return f"valores invalidos: {e}"