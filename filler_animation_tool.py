import time


# Affiche la barre de progression
def display_slider(
    current_level: int, max_level: int, icon: str, filler_icon: str, base_icon: str
):
    """
    Affiche la barre de progression sous forme de texte

    Arguments :
        current_level (int) : Le niveau actuel de progression.
        max_level (int) : Le niveau maximal de la barre (longueur totale).
        icon (str) : L'icône affichée au début de la barre de progression.
        filler_icon (str) : L'icône de remplissage pour représenter la progression.
        base_icon (str) : L'icône de base pour représenter la partie restante.
    """
    # Affiche la barre de progression en une seule ligne, en écrasant l'ancienne
    print(
        "["
        + icon
        + " "
        + current_level * filler_icon  # Partie remplie
        + (max_level - current_level) * base_icon  # Partie non remplie
        + "]",
        end="\r",  # Utilise \r pour revenir au début de la ligne sans en créer une nouvelle,
    )


# Fonction principale pour animer la barre de progression sur une durée donnée
def slider(duration: int, bar_lenght: int, icon: str, filler_icon: str, base_icon: str):
    """
    Crée une barre de progression animée qui dure pendant une période définie.

    Arguments :
        duration (int) : La durée totale de la progression, en secondes.
        bar_lenght (int) : La longueur totale de la barre de progression (nombre de niveaux).
        icon (str) : L'icône affichée au début de la barre de progression.
        filler_icon (str) : L'icône de remplissage pour représenter la progression.
        base_icon (str) : L'icône de base pour représenter la partie restante.
    """
    run: bool = True
    # Durée pour chaque niveau de progression
    duration_by_level: float = duration / bar_lenght
    start: float = time.time()  # Temps de départ
    old_level: int = -1  # Niveau précédent
    level: int = 0  # Niveau actuel
    end: int  # Variable pour enregistrer le temps de fin

    while run:
        end = time.time()  # Récupère l'heure actuelle

        # Calcule le niveau de progression actuel
        level = int(((end - start) / duration_by_level))

        # Affiche la barre de progression si le niveau a changé
        if level > old_level:
            old_level = level
            display_slider(level, bar_lenght, icon, filler_icon, base_icon)

        # Si la barre atteint la fin, arrête l'animation et passe à la ligne suivante
        if level >= bar_lenght:
            run = False
            print("\n")  # Saut de ligne après l'animation
