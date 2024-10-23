score_data = []

def get_score_data():
    
    if score_data == []:
        with open("data/score.txt", "r") as file:
                    for l in file.readlines():
                        if l != "\n":
                            score_data.append(l[:-1])
    print(score_data)
    return score_data

def save_score_data():

    with open("data/score.txt", "w") as file:
        for i in get_score_data():
            file.write(i + "\n")

def afficher_score():

    player_1_score = 0
    player_2_socre = 0

    
    print(f"perso 1: {player_1_score}   player_2_socre: {player_2_socre}")


def set_score(player_1_score: int, player_2_socre: int, jeux: str):
    new_data = []
    for data in score_data:
        if jeux not in data:
            new_data.append(data)
        else:
            pass

def get_score(jeux: str):

    player_1: int
    player_2: int

    score_data = get_score_data()

    for data in score_data:
        if jeux in data:
            p = 0
            cmpt = 0
            for c in data:
                if cmpt < 2:
                    if c == ":":
                        cmpt += 1
                    p += 1
            if "perso1" in data:
                player_1 = int(data[p:])
            else:
                player_2 = int(data[p:])

    return player_1,player_2

print(get_score("devinette"))