import unicodedata
from clear import special_print

# DISPLAY

# utility
def char_width(char: str )-> int:
    """
    Calcule la largeur d'un caractère en fonction de sa largeur East Asian.

    :param char: Caractère à évaluer
    :return: 2 si le caractère est "Wide" ou "Full-width", sinon 1
    """
    if unicodedata.east_asian_width(char) in ["W", "F"]:
        return 2
    else:
        return 1


def string_width(s: str) -> int:
    """
    Calcule la largeur totale d'une chaîne de caractères en considérant la largeur de chaque caractère.

    :param s: Chaîne de caractères
    :return: Largeur totale de la chaîne
    """
    return sum(char_width(char) for char in s)


def display_text(text: str, padding: int):
    """
    Affiche une ligne de texte formatée avec un padding dans une boite de largeur fixe de 40 caractères.

    :param text: Texte à afficher
    :param padding: Nombre d'espaces à ajouter avant le texte
    """

    text_display = "|" + " " * padding + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_center_text(text: str):
    """
    Affiche une ligne de texte centrée dans une boite de largeur fixe de 40 caractères.

    :param text: Texte à afficher
    """
    text_display: str = "|" + " " * (19 - int(string_width(text) / 2)) + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_line_jump():
    """
    Affiche une ligne vide dans une boîte de largeur fixe de 40 caractères.
    """
    special_print("|                                       |")


def display_paragraph(
    text: str, padding: int = 4, center: bool = False, jump_line: bool = False
):
    """
    Affiche un paragraphe formaté en sautant des lignes si nécessaire, et avec des options de centrage et de saut de ligne.

    :param text: Paragraphe à afficher
    :param padding: padding de chaque coté du paragraph
    :param center: Indique si le texte doit être centré
    :param jump_line: Indique si une ligne vide doit être affichée après chaque ligne de texte
    """

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
    """
    Affiche une boîte avec un titre, du texte et une icône.

    :param titre: Titre de la boîte
    :param text: Texte à afficher dans la boîte
    :param icon: Icône utilisée dans la ligne d'en-tête et de pied de page
    :param center_texte: Indique si le texte doit être centré
    :param padding: padding de chaque coté de la boite
    """
    special_print(f"\n{icon} -------------- Game ---------------{icon}")

    if titre != "":
        display_center_text(titre)
    if text != "":
        display_paragraph(text, padding, center_texte)
    else:
        display_line_jump()

    special_print(f"{icon} -----------------------------------{icon}\n")
