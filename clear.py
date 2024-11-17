import sys
import os
import math

lenght = 0

# clear system

def move_cursor_up(n: int):
    for _ in range(n):
        sys.stdout.write("\033[F")

def clear_line(n: int):
    for _ in range(n):
        special_print(" " * os.get_terminal_size().columns)

def clear(n: int):
    move_cursor_up(n)
    clear_line(n)
    move_cursor_up(n)
    sys.stdout.flush()

def clear_terminal():
    global lenght
    clear(lenght)
    lenght = 0

def special_print(text:str, end="\n"):
    global lenght
    add_lenght: int = 1
    #width: int = os.get_terminal_size().columns + math.ceil(len(text)/width)-1
    for c in text:
        if c == "\n":
            add_lenght +=1
    lenght += add_lenght 
    print(text, end=end)