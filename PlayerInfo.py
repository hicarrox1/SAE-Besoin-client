from dataclasses import dataclass

@dataclass
class PlayerInfo:
    pseudo: str = "..."
    is_bot: bool = False
    bot_level: int = 0
