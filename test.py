def afficher_plateau(plateau):
    
    plateau_affichage = ""
    for i in range(len(plateau)):
        plateau_affichage += " | ".join(plateau[i])+"\n"
        if i != len(plateau)-1:
            plateau_affichage += "---  " * 7 +"\n"
    plateau_affichage += "\n"
    
    print(plateau_affichage)

def verif_gagnant(plateau: list, jeton: str, colonne: int, ligne):

    for l in range(-1,2):
        for c in range(-1,2):

            if l == 0 and c == 0:
                pass
            else:
                cmpt = 1
                for i in range(1,4):
                    try:
                        if plateau[ligne+(i*l)][colonne+(i*c)] == jeton: cmpt += 1
                        if cmpt == 4: return True
                        
                    except:
                        pass
    return False



plateau = [["🔘" for _ in range(7)] for _ in range(6)]

plateau[-1][3] = "🔴"
plateau[-1][4] = "🔴"
plateau[-1][5] = "🔴"
plateau[-1][6] = "🔴"

afficher_plateau(plateau)

print(verif_gagnant(plateau,"🔴",3,len(plateau)-1))