import sys


def bouger_curseur_vers_haut(n: int):
    for _ in range(n):
        sys.stdout.write("\033[F")


def afficher_blanc(n: int):
    for _ in range(n):
        print(" " * 160)


def clear(n: int):
    sys.stdout.write("\n")
    n += 1
    bouger_curseur_vers_haut(n + 1)
    afficher_blanc(n)
    bouger_curseur_vers_haut(n)
    sys.stdout.flush()
