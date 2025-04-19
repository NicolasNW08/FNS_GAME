

import math

from src.components.module.levels_menu.validation import validation_free


def calculation_difficulty(min_val, max_val, attempts, text_label):
        try:
            
            rango = max_val - min_val + 1
            pasos_binarios = math.ceil(math.log2(rango))

            ratio = attempts / pasos_binarios

            if ratio >= 1.2:
                return 1
            elif ratio >= 1.0:
                return 2
            elif ratio >= 0.85:
                return 3
            elif ratio >= 0.7:
                return 4
            elif ratio >= 0.5:
                return 5
            elif ratio >= 0.3:
                return 6
            else:
                return 7

        except Exception as e:
            return f"valores invalidos: {e}"