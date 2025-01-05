from random import randint


def random_bot(limit: list) -> int:
    assert limit[0] < limit[1], "wrong limit"

    return randint(limit[0], limit[1])


def expert_bot_alumette(matche_count: int) -> int:
    best_option: int

    # La position perdante est celle où il reste 1 allumette (n == 1) ou un multiple de 4 + 1.
    if matche_count % 4 == 1:
        # Aucun coup possible pour gagner, l'adversaire a déjà une position perdante
        best_option = randint(1, 3)
    else:
        # Le meilleur coup consiste à ramener l'adversaire à une position perdante
        # Trouver le plus grand coup possible pour laisser un nombre d'allumettes multiple de 4 + 1
        for i in range(1, 4):
            if (matche_count - i) % 4 == 1:
                best_option = i  # On retourne le nombre d'allumettes à enlever

    return best_option


def middle_bot_devinette(greater: bool, old_move: int, number_limit: int):
    bot_move: int = 0
    if greater:
        bot_move = random_bot([old_move, number_limit[1]])
    else:
        bot_move = random_bot([number_limit[0], old_move])
    return bot_move


def expert_bot_devinette(greater: bool, old_move: int, number_limit: int):
    bot_move: int = 0

    if greater:
        bot_move = int((old_move + number_limit[1]) / 2)
    else:
        bot_move = int((old_move + number_limit[0]) / 2)

    return bot_move