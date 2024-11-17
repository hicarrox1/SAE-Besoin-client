saved_score_data = []
saved_game_data = []
saved_player_data = []

#data management

#get global data
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

#set global data
def save_data(path: str, data: list, encoding: str = "cp1252"):
    with open(path, "w", encoding=encoding) as file:
        for data_lines in data:
            for i in range(len(data_lines)):
                file.write(data_lines[i])
                if i != len(data_lines) - 1:
                    file.write(":")
            file.write("\n")

# get specific data 
def get_score_data():
    global saved_score_data
    return get_data("data/score.txt", saved_score_data)

def get_game_data():
    global saved_game_data
    save_game_data = get_data("data/game.txt", saved_game_data, "utf-8")
    return save_game_data

def get_player_data():
    global saved_player_data
    return get_data("data/player_name.txt", saved_player_data, "utf-8")

# set specific data 
def save_score_data():
    save_data("data/score.txt", get_score_data())

def save_game_data():
    save_data("data/game.txt", get_game_data(), "utf-8")

def save_player_data():
    save_data("data/player_name.txt", get_player_data(), "utf-8")

# utility
def find_data_line(searched_element: str, index: int, data: list) -> list:
    for line in data:
        if line[index] == searched_element:
            return line
    return []

def set_data_element(searched_element: str, searched_index: int, new_element: str, new_element_index: int, data: list):
    for line in data:
        if line[searched_index] == searched_element:
            line[new_element_index] = new_element

def sort_data(index: int, data: list, reverse: bool = False):
    for i in range(1, len(data)):
        cle = data[i]
        j = i - 1
        while j >= 0 and int(cle[index]) < int(data[j][index]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = cle
    if reverse:
        data.reverse()
    return data

# get special data
def get_player_name(id: int):
    data: list = find_data_line(str(id), 0, get_player_data())
    if data != []:
        return data[1]
    return "unknown"

def get_player_id(name: str):
    data = find_data_line(name, 1, get_player_data())
    if data != []:
        return int(data[0])
    return -1

def get_game_name(id: int):
    data = find_data_line(str(id), 0, get_game_data())
    if data != []:
        return data[1]
    return "unknown"

def get_game_id(name: str):
    data = find_data_line(name, 1, get_game_data())
    if data != []:
        return int(data[0])
    return -1

def get_score(player_id: int, game_name: str):
    score_line = find_data_line(str(player_id), 0, get_score_data())
    assert score_line != [], f"se jeux: {game_name}, n'existe pas"
    return int(score_line[get_game_id(game_name)+1])
    
def get_top_score(game_name: str, n:int):
    game_id: int = get_game_id(game_name)
    assert game_id != -1, f"se jeux: {game_name}, n'existe pas"
    score_data: list = sort_data(game_id+1,get_score_data(),True)
    
    players_score: list = []
    for line in score_data[:n]:
        players_score.append([line[0],line[game_id+1]])
    return players_score

# set special data
def add_score_line(player_index: int):
    score_data = get_score_data()
    score_data.append([str(player_index),"0","0","0","0"])
    save_score_data()

def add_player(name: str, icon: str):
    player_data: list = get_player_data()
    player_index: int = len(player_data)
    player_data.append([str(player_index), name, icon])
    add_score_line(player_index)
    save_player_data()

def set_player_icon(player_name: str, icon: str):
    player_data: list = get_player_data()

    set_data_element(player_name,1,icon,2, player_data)
    save_player_data()

def add_score_point(player_name: str, game_name: str, add_point: int):
    player_id: int = get_player_id(player_name)
    game_id: int = get_game_id(game_name)
    score: int = get_score(player_id,game_name)
    score += add_point
    assert game_id != -1 and player_id != -1, "valeur invalide"
    set_data_element(str(player_id),0,str(score),game_id+1,get_score_data())
    save_score_data()
