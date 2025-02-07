import random
from tkinter import *
import random

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#775e65", 4: "#775e65", 8: "#f9f6f2", 16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")
KEY_UP = "w"
KEY_DOWN = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"

matrix = []
grid_cells = []
mainframe = Frame()


def init_matrix():
    for i in range(GRID_LEN):
        matrix.append([0] * GRID_LEN)
    add_two()
    add_two()


def add_two():
    a = random.randint(0, GRID_LEN - 1)
    b = random.randint(0, GRID_LEN - 1)
    while matrix[a][b] != 0:
        a = random.randint(0, GRID_LEN - 1)
        b = random.randint(0, GRID_LEN - 1)
    matrix[a][b] = 2


def update_grid_cell():
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j] == 0:
                grid_cells[i][j].configure(text='', bg=BACKGROUND_COLOR_CELL_EMPTY)
            else:
                grid_cells[i][j].configure(text=str(matrix[i][j]), bg=BACKGROUND_COLOR_DICT,
                                           fg=CELL_COLOR_DICT[matrix[i][j]])


def init_grid():
    background = Frame(bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
    background.grid()
    for i in range(GRID_LEN):
        grid_row = []
        for j in range(GRID_LEN):
            cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
            cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
            t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=5,
                      height=2)
            t.grid()
            grid_row.append(t)
        grid_cells.append(grid_row)


def cover_up(mat):
    new = []
    for i in range(len(mat)):
        new.append([0] * len(mat))
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def main():
    init_grid()
    init_matrix()
    mainloop()


if __name__ == "__main__":
    main()
