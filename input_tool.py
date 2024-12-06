import sys
import msvcrt
from clear import special_input, clear_one_line, special_print


# INPUT
def ask_int(question: str, default: int, hide: bool = False):
    choice: int = default
    try:
        if hide:
            choice = int(hide_input(question))
        else:
            choice = int(special_input(question))
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choice


def ask_str(question: str, default: str, hide: bool = False):
    choice: str = default
    try:
        if hide:
            choice = hide_input(question)
        else:
            choice = special_input(question)
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choice


def hide_input(text: str):
    special_print(text, end="", flush=True)
    user_inputs: str = ""
    check: bool = True
    while check:
        char = msvcrt.getch()
        if char == b"\r":  # Entrée
            check = False
        elif char == b"\x08":  # Retour arrière
            if len(user_inputs) > 0:
                user_inputs = user_inputs[:-1]
                sys.stdout.write("\b \b")  # Efface le dernier caractère
                sys.stdout.flush()
        else:
            user_inputs += char.decode()
            sys.stdout.write("*")
            sys.stdout.flush()
    special_print("")
    return user_inputs
