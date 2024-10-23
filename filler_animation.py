import time


def set_level(
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


def launch_load_anim(
    duration: int, bar_lenght: int, icon: str, filler_icon: str, base_icon: str
):
    game = True
    duration = duration
    bar_lenght = bar_lenght
    duration_by_level = duration / bar_lenght
    start = time.time()
    old_level = -1
    level = 0

    while game:
        end = time.time()
        level = int(((end - start) / duration_by_level))
        if level > old_level:
            old_level = level
            set_level(level, bar_lenght, icon, filler_icon, base_icon)

        if level >= bar_lenght:
            game = False
            print("\n")
