import toolbox
from clear import clear
import data

def change_name():

    player1 = data.get_name(1)
    player2 = data.get_name(2)

    toolbox.afffichage_box(texte=f"quelle joueur veut changer de nom:\n1. {player1} \n2. {player2}",center_texte=True, padding= 2)
    choix = int(input("Votre choix : "))
    clear(7)

    name = input("\nnouveau nom : ")
    clear(1)

    data.set_name(choix,name)