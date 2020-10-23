# https://prnt.sc/oo53q6
from tkinter import *

root = Tk()
# root.geometry('500x300+1000+500')


def getColor(colorName, colorCode):
    ntr.delete(0, END)
    ntr.insert(0, colorCode)
    lbl['text'] = colorName
    lbl['fg'] = colorCode


lbl = Label(root, bg='white', font='Times 25 bold')
lbl.pack(fill=X)

ntr = Entry(root, justify='center', font='Times 15 bold')
ntr.pack(fill=X)

colors = {
    '#ff0000': "Red",
    '#ff7d00': 'Orange',
    '#ffff00': 'Yellow',
    '#00ff00': 'Green',
    '#007dff': 'Blue',
    '#0000ff': 'Dark Blue',
    '#7d00ff': 'Violet'
}

for k, v in colors.items():
    Button(root, bg=k, command=lambda colorName=v, colorCode=k: getColor(
        colorName, colorCode)).pack(fill=X)


root.mainloop()
