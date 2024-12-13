import unicodedata
from clear import special_print

# DISPLAY


# utility
def char_width(char: str) -> int:
    """
    Calcule la largeur d'un caractère en fonction de sa largeur East Asian.

    Arguments :
        char (str) : Caractère à évaluer

    Retourne :
        int : 2 si le caractère est "Wide" ou "Full-width", sinon 1
    """
    longeur: int = 1  # Valeur par défaut pour un caractère de largeur 1
    # Vérifie si le caractère est large
    if unicodedata.east_asian_width(char) in ["W", "F"]:
        longeur = 2
    return longeur


def string_width(s: str) -> int:
    """
    Calcule la largeur totale d'une chaîne de caractères en considérant la largeur de chaque caractère.

    Arguments :
        s (str) : Chaîne de caractères

    Retourne :
        int : Largeur totale de la chaîne
    """
    # Somme des largeurs de chaque caractère
    return sum(char_width(char) for char in s)


def display_text(text: str, padding: int):
    """
    Affiche une ligne de texte formatée avec un padding dans une boîte de largeur fixe de 40 caractères.

    Arguments :
        text (str) : Texte à afficher
        padding (int) : Nombre d'espaces à ajouter avant le texte
    """

    text_display = "|" + " " * padding + text
    text_display = text_display + " " * (40 - int(string_width(text_display))) + "|"
    special_print(text_display)


def display_center_text(text: str):
    """
    Affiche une ligne de texte centrée dans une boîte de largeur fixe de 40 caractères.

    Arguments :
        text (str) : Texte à afficher
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

    Arguments :
        text (str) : Paragraphe à afficher
        padding (int) : padding de chaque coté du paragraphe
        center (bool) : Indique si le texte doit être centré
        jump_line (bool) : Indique si une ligne vide doit être affichée après chaque ligne de texte
    """

    # affichage du texte en sautant de ligne si nécessaire et en ne coupant pas les mots
    all_text_line: list = []
    text_line: str = ""
    mot: str = ""
    for c in text:
        if c == " " or c == "\n":
            # Ajoute le mot à la ligne courante
            if text_line == "" and len(mot) > 1:
                text_line += mot
            else:
                text_line += " " + mot
            mot = ""

            # Si un saut de ligne, ajoute la ligne actuelle à la liste
            if c == "\n":
                all_text_line.append(text_line)
                text_line = ""
        else:
            mot += c

            # Vérifie si le mot dépasse la largeur et commence une nouvelle ligne
            if string_width(mot) >= 39 - (2 * padding):
                if text_line != "":
                    all_text_line.append(text_line)
                all_text_line.append(mot)
                mot = ""
                text_line = ""

        # Vérifie si la ligne courante dépasse la largeur limite
        if (string_width(text_line) + string_width(mot)) >= 39 - (2 * padding):
            all_text_line.append(text_line)
            text_line = ""

    # Ajoute le dernier mot ou la ligne restante
    if mot != "":
        if text_line == "":
            text_line += mot
        else:
            text_line += " " + mot
    if text_line != "":
        all_text_line.append(text_line)

    # Affiche chaque ligne, avec ou sans saut de ligne et en le centrant ou non
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

    Arguments :
        titre (str) : Titre de la boîte
        text (str) : Texte à afficher dans la boîte
        icon (str) : Icône utilisée dans la ligne d'en-tête et de pied de page
        center_texte (bool) : Indique si le texte doit être centré
        padding (int) : padding de chaque coté de la boîte
    """
    # Affiche l'en-tête de la boîte avec l'icône
    special_print(f"\n{icon} -------------- Game ---------------{icon}")

    # Affiche le titre si fourni
    if titre != "":
        display_center_text(titre)
    # Affiche le texte si fourni, sinon saute une ligne
    if text != "":
        display_paragraph(text, padding, center_texte)
    else:
        display_line_jump()

    # Affiche le pied de la boîte avec l'icône
    special_print(f"{icon} -----------------------------------{icon}\n")
