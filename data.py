score_data = []
game_data = []


def get_data_from_lines(lines: str):
    data = []
    current_data = ""
    for c in lines:
        current_data += c
        if c == ":" or c == "\n":
            data.append(current_data[:-1])
            current_data = ""
    return data


def get_data(path: str, data_liste: list, encoding: str = "cp1252"):
    if data_liste == []:
        with open(path, "r", encoding=encoding) as file:
            for lines in file.readlines():
                if lines != "\n":
                    data_liste.append(get_data_from_lines(lines))
    return data_liste


def save_data(path: str, data: list, encoding: str = "cp1252"):
    with open(path, "w", encoding=encoding) as file:
        for data_lines in data:
            for data in data_lines:
                file.write(data)
                if data != data_lines[-1]:
                    file.write(":")
            file.write("\n")


def get_score_data():
    global score_data

    return get_data("data/score.txt", score_data)


def get_game_data():
    global game_data

    return get_data("data/game.txt", game_data, "utf-8")


def save_score_data():
    save_data("data/score.txt", get_score_data())


def save_game_data():
    save_data("data/game.txt", get_game_data(), "utf-8")


def get_select_game(game: str):
    game_data = get_game_data()
    for data in game_data:
        if data[0] == game:
            return data


def set_score(player_1_score: int, player_2_score: int, jeux: str):
    score_data = get_score_data()
    for data_lines in score_data:
        if data_lines[1] == jeux:
            if data_lines[0] == "player1":
                data_lines[2] = str(player_1_score)
            elif data_lines[0] == "player2":
                data_lines[2] = str(player_2_score)


def get_score(jeux: str):
    score_data = get_score_data()

    for data_lines in score_data:
        if data_lines[1] == jeux:
            if data_lines[0] == "player1":
                player_1_score = data_lines[2]
            elif data_lines[0] == "player2":
                player_2_score = data_lines[2]

    return [player_1_score, player_2_score]


def afficher_score(jeux: str):
    score = get_score(jeux)
    player_1_score = score[0]
    player_2_score = score[1]
    print(f"perso 1: {player_1_score}   perso 2: {player_2_score}")
