#import toolbox
player1:int = None
player2:int = None

def get_nombre_choisi():
        player1=int(input("Player1 Saisir un nombre : "))

        while player1<1:
            player1=int(input("nombre trop petit : "))
        return player1

player2=int(input("Saisir un nombre"))

if player2==player1:
    print("c'est gagné")
else:
    player2=int(input("Saisir un nombre"))
    
if __name__ == "__main__":
    score:int

nombre_choisi = get_nombre_choisi()

print(nombre_choisi)