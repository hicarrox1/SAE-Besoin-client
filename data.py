# Variables Global qui vont contenir les donée pendant l'éxécution
saved_score_data = []
saved_game_data = []
saved_player_data = []

# Gestion des données Général


# Récupère les données d'un fichier texte et les transforme en une liste
def get_data_from_lines(lines: str):
    """
    Transforme une ligne de données en une liste de valeurs en fonction du délimiteur `:` et `&`.

    Arguments :
        lines (str) : Une chaîne de caractères représentant une ligne dans le fichier.

    Retourne :
        list : Une liste de données séparées.
    """
    data: list = []
    current_data: str = ""
    for c in lines:
        # Remplace `&` par un saut de ligne
        if c == "&":
            current_data += "\n"
        elif c == ":" or c == "\n":
            data.append(current_data)  # Ajoute l'élément actuel à la liste
            current_data = ""  # Réinitialise l'élément courant
        else:
            current_data += c  # Ajoute le caractère courant à l'élément
    return data


# Récupère les données depuis un fichier et les stocke dans la liste appropriée
def get_data(path: str, data_liste: list, encoding: str = "cp1252"):
    """
    Récupère les données d'un fichier et les charge dans la liste spécifiée.

    Arguments :
        path (str) : Le chemin du fichier à lire.
        data_liste (list) : La liste où les données seront stockées.
        encoding (str) : L'encodage du fichier. Par défaut 'cp1252'.

    Retourne :
        list : La liste des données chargées.
    """
    if data_liste == []:  # Verifie si les donée ne sont pas déja chargé
        with open(path, "r", encoding=encoding) as file:
            for lines in file.readlines():
                if lines != "\n":
                    data_liste.append(get_data_from_lines(lines))
    return data_liste


# Sauvegarde les données dans un fichier
def save_data(path: str, data: list, encoding: str = "cp1252"):
    """
    Sauvegarde les données dans un fichier.

    Arguments :
        path (str) : Le chemin du fichier où les données doivent être sauvegardées.
        data (list) : Les données à sauvegarder.
        encoding (str) : L'encodage du fichier. Par défaut 'cp1252'.
    """

    with open(path, "w", encoding=encoding) as file:
        for data_lines in data:
            for i in range(len(data_lines)):
                file.write(data_lines[i])
                if i != len(data_lines) - 1:
                    file.write(":")  # Ajoute le séparateur `:` entre les éléments
            file.write("\n")  # Ajoute une nouvelle ligne après chaque enregistrement


# Récupère les données spécifiques


def get_score_data():
    """
    Récupère les données de score depuis le fichier `score.txt`.

    Retourne :
        list : Les données de score.
    """
    global saved_score_data
    return get_data("data/score.txt", saved_score_data)


def get_game_data():
    """
    Récupère les données de jeu depuis le fichier `game.txt`.

    Retourne :
        list : Les données de jeu.
    """
    global saved_game_data
    save_game_data = get_data("data/game.txt", saved_game_data, "utf-8")
    return save_game_data


def get_player_data():
    """
    Récupère les données des joueurs depuis le fichier `player_name.txt`.

    Retourne :
        list : Les données des joueurs.
    """
    global saved_player_data
    return get_data("data/player_name.txt", saved_player_data, "utf-8")


# Sauvegarde les données spécifiques


def save_score_data():
    """
    Sauvegarde les données de score dans le fichier `score.txt`.
    """
    save_data("data/score.txt", get_score_data())


def save_game_data():
    """
    Sauvegarde les données de jeu dans le fichier `game.txt`.
    """
    save_data("data/game.txt", get_game_data(), "utf-8")


def save_player_data():
    """
    Sauvegarde les données des joueurs dans le fichier `player_name.txt`.
    """
    save_data("data/player_name.txt", get_player_data(), "utf-8")


# Utilitaires pour manipuler les données


def find_data_line(searched_element: str, index: int, data: list) -> list:
    """
    Recherche une ligne spécifique dans les données en fonction d'un élément donné et de son index.

    Arguments :
        searched_element (str) : L'élément à rechercher.
        index (int) : L'index de l'élément dans la ligne.
        data (list) : Les données dans lesquelles effectuer la recherche.

    Retourne :
        list : La ligne correspondante si trouvée, sinon une liste vide.
    """
    return_list: list = []
    for line in data:
        if line[index] == searched_element:
            return_list = line
    return return_list  # Retourne une liste vide si aucun élément n'est trouvé


def set_data_element(
    searched_element: str,
    searched_index: int,
    new_element: str,
    new_element_index: int,
    data: list,
):
    """
    Modifie un élément dans les données en fonction d'un élément recherché et de ses indices.

    Arguments :
        searched_element (str) : L'élément à rechercher.
        searched_index (int) : L'index de l'élément à rechercher.
        new_element (str) : Le nouvel élément à ajouter.
        new_element_index (int) : L'index où remplacer l'élément dans la ligne.
        data (list) : Les données dans lesquelles effectuer la modification.
    """
    for line in data:
        if line[searched_index] == searched_element:
            line[new_element_index] = new_element


def sort_integer_data(index: int, data: list, reverse: bool = False):
    """
    Trie une liste de données en fonction d'un élément entier à un index spécifique dans chaque sous-liste.

    Arguments :
        index (int) : L'index de l'élément à trier dans chaque sous-liste.
        data (list) : La liste de sous-listes à trier.
        reverse (bool) : Si True, trie en ordre décroissant. Par défaut, False (ordre croissant).

    Retourne :
        list : Une nouvelle liste triée selon l'élément à l'index spécifié.
    """

    # Fonction interne pour obtenir la valeur entière à l'index spécifié dans chaque sous-liste
    def sort_key(element: list):
        return int(element[index])  # Convertit l'élément à l'index donné en entier

    # Trie les données en utilisant la fonction sort_key comme clé de tri et retourne la liste triée
    return sorted(data, reverse=reverse, key=sort_key)


# Récupère des données spécifiques


def get_player_name(id: int):
    """
    Récupère le nom d'un joueur en fonction de son ID.

    Arguments :
        id (int) : L'ID du joueur.

    Retourne :
        str : Le nom du joueur ou "unknown" si non trouvé.
    """
    data: list = find_data_line(str(id), 0, get_player_data())
    player_name: str = "unknown"
    if data != []:
        player_name = data[1]  # Retourne le nom du joueur
    return player_name


def get_player_id(name: str):
    """
    Récupère l'ID d'un joueur en fonction de son nom.

    Arguments :
        name (str) : Le nom du joueur.

    Retourne :
        int : L'ID du joueur ou -1 si non trouvé.
    """
    data = find_data_line(name, 1, get_player_data())
    player_id: int = -1
    if data != []:
        player_id = int(data[0])  # Retourne l'ID du joueur
    return player_id


def get_player_icon(name: str):
    """
    Récupère l'icône d'un joueur en fonction de son nom.

    Arguments :
        name (str) : Le nom du joueur.

    Retourne :
        str : L'icône du joueur ou "🦖" par défaut si non trouvé.
    """
    data = find_data_line(name, 1, get_player_data())
    player_icon: str = "🦖"  # Icône par défaut
    if data != []:
        player_icon = data[2]  # Retourne l'icône du joueur
    return player_icon


def get_game_line(game_name: str):
    """
    Récupère les données d'un jeu en fonction de son nom.

    Arguments :
        game_name (str) : Le nom du jeu.

    Retourne :
        list : Les données du jeu ou une liste vide si non trouvé.
    """
    return find_data_line(game_name, 1, get_game_data())


def get_game_name(id: int):
    """
    Récupère le nom d'un jeu en fonction de son ID.

    Arguments :
        id (int) : L'ID du jeu.

    Retourne :
        str : Le nom du jeu ou "unknown" si non trouvé.
    """
    data = find_data_line(str(id), 0, get_game_data())
    game_name: str = "unknown"
    if data != []:
        game_name = data[1]
    return game_name


def get_game_id(name: str):
    """
    Récupère l'ID d'un jeu en fonction de son nom.

    Arguments :
        name (str) : Le nom du jeu.

    Retourne :
        int : L'ID du jeu ou -1 si non trouvé.
    """
    data = find_data_line(name, 1, get_game_data())
    game_id: int = -1
    if data != []:
        game_id = int(data[0])
    return game_id


def get_score(player_id: int, game_name: str):
    """
    Récupère le score d'un joueur pour un jeu donné.

    Arguments :
        player_id (int) : L'ID du joueur.
        game_name (str) : Le nom du jeu.

    Retourne :
        int : Le score du joueur pour le jeu.
    """
    score_line = find_data_line(str(player_id), 0, get_score_data())
    assert score_line != [], f"se jeux: {game_name}, n'existe pas"
    return int(score_line[get_game_id(game_name) + 1])  # Retourne le score du joueur


def get_top_score(game_name: str, n: int):
    """
    Récupère les meilleurs scores pour un jeu donné.

    Arguments :
        game_name (str) : Le nom du jeu.
        n (int) : Le nombre de meilleurs scores à récupérer.

    Retourne :
        list : Une liste des n meilleurs scores avec les ID des joueurs et leurs scores.
    """
    game_id: int = get_game_id(game_name)
    assert game_id != -1, f"se jeux: {game_name}, n'existe pas"
    # Trie les scores par ordre décroissant
    score_data: list = sort_integer_data(game_id + 1, get_score_data(), True)

    players_score: list = []
    for line in score_data[:n]:
        # Ajoute les scores des meilleurs joueurs
        players_score.append([line[0], line[game_id + 1]])
    return players_score


def get_player_scores(player_id: int) -> list:
    """
    Récupère tous les scores d'un joueur pour tous les jeux.

    Arguments :
        player_id (int) : L'ID du joueur.

    Retourne :
        list : Une liste de scores pour tous les jeux.
    """
    player_scores: list = find_data_line(str(player_id), 0, get_score_data())

    return player_scores[1:]  # Retourne les scores du joueur


# Ajout de nouvelles données


def add_score_line(player_index: int):
    """
    Ajoute une nouvelle ligne de score pour un joueur dans les données.

    Arguments :
        player_index (int) : L'index du joueur pour lequel ajouter la ligne.
    """
    score_data = get_score_data()
    score_data.append([str(player_index), "0", "0", "0", "0"])
    save_score_data()


def add_player(name: str, icon: str):
    """
    Ajoute un nouveau joueur avec son nom et son icône.

    Arguments :
        name (str) : Le nom du joueur.
        icon (str) : L'icône du joueur.
    """
    # Vérifie si le nom n'existe pas déjà
    assert get_player_id(name) == -1, "Erreur le nom est deja pris"
    player_data: list = get_player_data()
    # L'index est basé sur la longueur actuelle de la liste
    player_index: int = len(player_data)
    # Ajoute le joueur à la liste
    player_data.append([str(player_index), name, icon])
    # Ajoute une ligne de score pour ce joueur
    add_score_line(player_index)
    save_player_data()


def set_player_icon(player_name: str, icon: str):
    """
    Modifie l'icône d'un joueur.

    Arguments :
        player_name (str) : Le nom du joueur.
        icon (str) : La nouvelle icône du joueur.
    """
    player_data: list = get_player_data()
    # Modifie l'icône du joueur dans les données
    set_data_element(player_name, 1, icon, 2, player_data)
    save_player_data()


def set_player_name(player_name: str, new_player_name: str):
    """
    Modifie le nom d'un joueur.

    Arguments :
        player_name (str) : Le nom du joueur.
        new_player_name (str) : Le nouveau nom du joueur.

    """
    player_data: list = get_player_data()
    # Vérifie si le nouveau nom n'existe pas déjà
    assert get_player_id(new_player_name) == -1, "Erreur le nom est deja pris"
    # Modifie le nom du joueur dans les données
    set_data_element(player_name, 1, new_player_name, 1, player_data)
    save_player_data()


def add_score_point(player_name: str, game_name: str, add_point: int):
    """
    Ajoute des points au score d'un joueur dans un jeu spécifique.

    Arguments :
        player_name (str) : Le nom du joueur.
        game_name (str) : Le nom du jeu.
        add_point (int) : Le nombre de points à ajouter.
    """
    player_id: int = get_player_id(player_name)
    game_id: int = get_game_id(game_name)
    score: int = get_score(player_id, game_name)
    # Ajoute les points au score actuel
    score += add_point
    # Vérifie que les données sont valides
    assert game_id != -1 and player_id != -1, "valeur invalide"
    # Met à jour le score
    set_data_element(str(player_id), 0, str(score), game_id + 1, get_score_data())
    save_score_data()


def get_player_score_text(player_id: int) -> str:
    """
    Récupère les scores d'un joueur donné.
    et les retourne sous forme de texte.

    Arguments :
        player_id (int) : ID du joueur.
    retourne :
        str : Les scores du joueur.
    """
    # Récupération des scores du joueur
    texte: str = ""
    scores: list = get_player_scores(player_id)
    for i in range(len(scores)):
        texte += f"{get_game_name(i)} : {scores[i]}\n"

    return texte
