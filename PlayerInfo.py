from dataclasses import dataclass


# PlayerInfo class
@dataclass
class PlayerInfo:
    # Classe qui contient les informations d'un joueur
    pseudo: str = "..."
    is_bot: bool = False
    bot_level: int = 0
    icon: str = "🌵"
