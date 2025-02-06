from tkinter import *


background = Frame(bg="#fff000", width=400, height=400)
background.grid()

row = 1
column = 1
for i in range(4):
    for j in range(3):
        btn = Button(background, text=f"{i}{j}")
        btn.grid(row=i, column=j)


mainloop()