import getpass
from clear import special_input, clear_one_line, special_print


# INPUT
def ask_int(question: str, default: int):
    choice: int = default
    try:
        choice = int(special_input(question))
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choice


def ask_str(question: str, default: str):
    choice: str = default
    try:
        choice = special_input(question)
        clear_one_line()
    except ValueError:
        clear_one_line()
    return choice