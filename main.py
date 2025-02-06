import random
from tkinter import *

SIZE = 400
GRID_LEN = 4
GRID_PAD = 10

GRID_BG_COLOR = "#92877D"
CELL_BG_COLOR = "#9E948A"
BG_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                 128: "#edcf72",256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc33e"}
CELL_COLOR_DICT = {2: "#775e65", 4: "#775e65", 8: "#f9f6f2", 16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                 128: "#f9f6f2",256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")
KEY_UP = "w"
KEY_DOWN = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"

matrix = []
grid_cell = []
mainframe = Frame()

def init_grid():
    background = Frame(bg=GRID_BG_COLOR, width=SIZE, height=SIZE)
    background.grid()
    mainloop()


init_grid()