import unicodedata
from clear import special_print

# DISPLAY

# utility


def char_width(char):
    if unicodedata.east_asian_width(char) in ["W", "F"]:
        return 2
    else:
        return 1


def string_width(s):
    return sum(char_width(char) for char in s)


def display_text(text: str, padding: int):
    text_display = "|" + " " * padding + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_center_text(text: str):
    text_display: str = "|" + " " * (19 - int(string_width(text) / 2)) + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_line_jump():
    special_print("|                                       |")


def display_paragraph(
    text: str, padding: int = 4, center: bool = False, jump_line: bool = False
):
    # affichage du texte en sautant de ligne si nécessaire
    all_text_line: list = []
    text_line: str = ""
    mot: str = ""
    for c in text:
        if c == " " or c == "\n":
            if text_line == "" and len(mot) > 1:
                text_line += mot
            else:
                text_line += " " + mot
            mot = ""
            if c == "\n":
                all_text_line.append(text_line)
                text_line = ""
        else:
            mot += c
            if string_width(mot) >= 39 - (2 * padding):
                if text_line != "":
                    all_text_line.append(text_line)
                all_text_line.append(mot)
                mot = ""
                text_line = ""
        if (string_width(text_line) + string_width(mot)) >= 39 - (2 * padding):
            all_text_line.append(text_line)
            text_line = ""

    if mot != "":
        if text_line == "":
            text_line += mot
        else:
            text_line += " " + mot
    if text_line != "":
        all_text_line.append(text_line)

    for ligne in all_text_line:
        if center:
            display_center_text(ligne)
        else:
            display_text(ligne, padding)
        if jump_line:
            display_line_jump()


def display_box(
    titre: str = "",
    text: str = "",
    icon: str = "🔘",
    center_texte: bool = False,
    padding=4,
):
    special_print(f"\n{icon} -------------- Game ---------------{icon}")

    if titre != "":
        display_center_text(titre)
    if text != "":
        display_paragraph(text, padding, center_texte)
    else:
        display_line_jump()

    special_print(f"{icon} -----------------------------------{icon}\n")
