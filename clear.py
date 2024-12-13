import sys
import os

# Variable globale pour suivre le nombre de lignes actuellement occupées dans le terminal
lenght: int = 0


# Effacement des lignes


# Déplace le curseur du terminal vers le haut
def move_cursor_up(n: int):
    """
    Déplace le curseur du terminal vers le haut de `n` lignes en utilisant
    des codes d'échappement ANSI.

    Arguments :
        n (int) : Le nombre de lignes à remonter.
    """
    for _ in range(n):
        sys.stdout.write("\033[F")  # Déplace le curseur d'une ligne vers le haut


# Efface un nombre donné de lignes dans le terminal
def clear(n: int):
    """
    Efface `n` lignes au-dessus de la position actuelle du curseur, réinitialise
    la position du curseur, puis vide la sortie du terminal.

    Arguments :
        n (int) : Le nombre de lignes à effacer.
    """
    move_cursor_up(n)

    for _ in range(n):
        # Remplace la ligne par des espaces en fonction de la taille du terminal
        special_print(" " * os.get_terminal_size().columns)

    move_cursor_up(n)  # Réinitialise la position du curseur
    sys.stdout.flush()  # Vide le buffer pour un affichage immédiat


# Efface tout le contenu du terminal
def clear_terminal():
    """Efface toutes les lignes."""
    global lenght
    clear(lenght)
    lenght = 0  # Réinitialise `lenght` à 0


# Efface une seule ligne dans le terminal
def clear_one_line():
    """
    Efface une ligne dans le terminal et ajuste la variable globale `lenght` en conséquence.
    """
    global lenght
    clear(1)
    lenght -= 2
    if lenght <= 0:  # Assure que `lenght` ne descend pas en dessous de 0
        lenght = 0


# Gestion des lignes affichées


# Calcule le nombre de lignes qu'un texte occupera dans le terminal
def get_number_ligne(texte: str):
    """
    Calcule le nombre de lignes occupées par un texte donné, en prenant en compte
    les sauts de ligne.

    Arguments :
        texte (str) : Le texte à analyser.

    Retourne :
        int : Le nombre de lignes occupées.
    """
    add_lenght: int = 1
    for c in texte:
        if c == "\n":
            # Compte un saut de ligne comme une ligne supplémentaire
            add_lenght += 1
    return add_lenght


# Affiche du texte dans le terminal tout en mettant à jour la variable globale `lenght`
def special_print(text: str, end="\n", flush=False):
    """
    Affiche du texte dans le terminal tout en suivant le nombre de lignes occupées.

    Arguments :
        text (str) : Le texte à afficher.
        end (str) : La chaîne ajoutée après le texte (par défaut, un saut de ligne).
        flush (bool) : Si vrai, force la vidange de la sortie (par défaut, False).
    """
    global lenght
    # Ajoute le nombre de lignes occupées par le texte à la variable globale `lenght`
    lenght += get_number_ligne(text)

    # Affiche le texte
    print(text, end=end, flush=flush)


# Affiche un message d'invite et capture une entrée utilisateur
def special_input(text: str):
    """
    Affiche un message d'invite et capture une entrée utilisateur, tout en suivant
    le nombre de lignes occupées.

    Arguments :
        text (str) : Le message d'invite à afficher.

    Retourne :
        str : L'entrée de l'utilisateur.
    """
    global lenght
    # Ajoute le nombre de lignes occupées par le texte à la variable globale `lenght`
    lenght += get_number_ligne(text)

    # Retourne l'entrée utilisateur
    return input(text)
