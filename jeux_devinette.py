import toolbox
import data
from clear import clear
import time

def get_nombre_choisi(name_player_choose):
    number_choose = int(input(f"{name_player_choose}, saisissez un nombre : "))
    clear(0)
    while number_choose < 1 or number_choose > 1000:
        number_choose = int(input("Nombre invalide, veuillez choisir un nombre entre 1 et 1000 : "))
        clear(0)
    return number_choose

def deviner_nombre(number_choose, name_player_guess):
    number_test = None
    print("---------------------------")
    while number_test != number_choose:
        number_test = int(input(f"{name_player_guess}, devinez le nombre : "))
        clear(1)
        if number_test == number_choose:
            print("C'est gagné ! 🟰")
            toolbox.affiche_victoire(name_player_guess,1)
            data.add_score(1,data.get_name_id(name_player_guess),"devinette")
            time.sleep(2)
            clear(6)
        elif number_test < number_choose:
            print("Trop petit ↘️")
        else:
            print("Trop grand ↗️")

def launch(player_begin: int):

    game = True
    choix : int

    player_1 = data.get_name(player_begin)
    player_2 = data.get_name((player_begin+1)%2)
    current_player = player_1

    while game:
        
        nombre_a_deviner = get_nombre_choisi(current_player)
        deviner_nombre(nombre_a_deviner, player_2 if current_player == player_1 else player_1)
        current_player = player_2 if current_player == player_1 else player_1
        nombre_a_deviner = get_nombre_choisi(current_player)
        deviner_nombre(nombre_a_deviner, player_2 if current_player == player_1 else player_1)

        print('voulez vous rejouer taper 0. Non 1. Oui')
        choix = int(input(""))

        time.sleep(1)
        clear(1)

        if choix == 1:
            game = True
            current_player = player_2 if current_player == player_1 else player_1
        else:
            game = False
