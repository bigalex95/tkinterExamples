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

Button(root, bg='#ff0000', command=lambda: getColor(
    'Red', '#ff0000')).pack(fill=X)
Button(root, bg='#ff7d00', command=lambda: getColor(
    'Orange', '#ff7d00')).pack(fill=X)
Button(root, bg='#ffff00', command=lambda: getColor(
    'Yellow', '#ffff00')).pack(fill=X)
Button(root, bg='#00ff00', command=lambda: getColor(
    'Green', '#00ff00')).pack(fill=X)
Button(root, bg='#007dff', command=lambda: getColor(
    'Blue', '#007dff')).pack(fill=X)
Button(root, bg='#0000ff', command=lambda: getColor(
    'Dark Blue', '#0000ff')).pack(fill=X)
Button(root, bg='#7d00ff', command=lambda: getColor(
    'Violet', '#7d00ff')).pack(fill=X)

root.mainloop()
