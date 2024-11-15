score_data = []
game_data = []
name_data = []


def get_data_from_lines(lines: str):
    data: list = []
    current_data: str = ""
    for c in lines:
        if c == "&":
            current_data += "\n"
        elif c == ":" or c == "\n":
            data.append(current_data)
            current_data = ""
        else:
            current_data += c
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
            for i in range(len(data_lines)):
                file.write(data_lines[i])
                if i != len(data_lines) - 1:
                    file.write(":")
            file.write("\n")


def get_score_data():
    global score_data

    return get_data("data/score.txt", score_data)


def get_game_data():
    global game_data

    return get_data("data/game.txt", game_data, "utf-8")


def get_name_data():
    global name_data

    return get_data("data/player_name.txt", name_data, "utf-8")


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
    global score_data
    score_data = get_score_data()
    for data_lines in score_data:
        if data_lines[1] == jeux:
            if data_lines[0] == "1":
                data_lines[2] = str(player_1_score)
            elif data_lines[0] == "2":
                data_lines[2] = str(player_2_score)

    save_data("data/score.txt", score_data)


def add_score(point_gain: int, player_id: int, jeux: str):
    score = get_score(jeux)
    score[player_id] += point_gain
    set_score(score[0], score[1], jeux)


def get_score(jeux: str):
    score_data = get_score_data()

    for data_lines in score_data:
        if data_lines[1] == jeux:
            if data_lines[0] == "1":
                player_1_score = int(data_lines[2])
            elif data_lines[0] == "2":
                player_2_score = int(data_lines[2])

    return [player_1_score, player_2_score]


def get_name(name_id: int):
    return get_name_data()[(name_id - 1)][1]


def get_name_id(name: str):
    name_data = get_name_data()
    for i in range(len(name_data)):
        if name in name_data[i]:
            return i


def set_name(name_id: int, name):
    name_data = get_name_data()[(name_id - 1)]

    name_data[1] = name

    save_data("data/player_name.txt", get_name_data(), "utf-8")
