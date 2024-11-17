import time


def display_slider(
    current_level: int, max_level: int, icon: str, filler_icon: str, base_icon: str
):
    print(
        "["
        + icon
        + " "
        + current_level * filler_icon
        + (max_level - current_level) * base_icon
        + "]",
        end="\r",
    )


def slider(duration: int, bar_lenght: int, icon: str, filler_icon: str, base_icon: str):
    run: bool = True
    duration: int = duration
    bar_lenght: int = bar_lenght
    duration_by_level: float = duration / bar_lenght
    start: float = time.time()
    old_level: int = -1
    level: int = 0
    end: int

    while run:
        end = time.time()
        level = int(((end - start) / duration_by_level))
        if level > old_level:
            old_level = level
            display_slider(level, bar_lenght, icon, filler_icon, base_icon)

        if level >= bar_lenght:
            run = False
            print("\n")
