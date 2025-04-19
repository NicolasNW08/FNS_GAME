import random

from src.language.es_ES import LEVELS_FREE_DIFFICULTY_DIALOGUES
from src.language.es_ES import LEVELS_VERSUS_DIFFICULTY_DIALOGUES, VERSUS_DIALOGUES


def random_dialog(difficulty):
    return random.choice(LEVELS_FREE_DIFFICULTY_DIALOGUES[difficulty])


def random_dialog_add_players(player_name):
    dialog = random.choice(VERSUS_DIALOGUES)
    return dialog.format(player=player_name)
    
def random_dialog_difficulty(difficulty):
    return random.choice(LEVELS_VERSUS_DIFFICULTY_DIALOGUES[difficulty])