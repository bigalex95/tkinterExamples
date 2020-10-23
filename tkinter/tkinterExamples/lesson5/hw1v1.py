# https://prnt.sc/oo53q6
from tkinter import *

root = Tk()
# root.geometry('500x300+1000+500')


def redBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#ff0000')
    lbl['text'] = 'Red'
    lbl['fg'] = '#ff0000'


def orangeBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#ff7d00')
    lbl['text'] = 'Orange'
    lbl['fg'] = '#ff7d00'


def yellowBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#ffff00')
    lbl['text'] = 'Yellow'
    lbl['fg'] = '#ffff00'


def greenBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#00ff00')
    lbl['text'] = 'Green'
    lbl['fg'] = '#00ff00'


def blueBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#007dff')
    lbl['text'] = 'Blue'
    lbl['fg'] = '#007dff'


def darkblueBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#0000ff')
    lbl['text'] = 'Dark Blue'
    lbl['fg'] = '#0000ff'


def violetBtn():
    ntr.delete(0, END)
    ntr.insert(0, '#7d00ff')
    lbl['text'] = 'Violet'
    lbl['fg'] = '#7d00ff'


lbl = Label(root, bg='white', font='Times 25 bold')
lbl.pack(fill=X)

ntr = Entry(root, justify='center', font='Times 15 bold')
ntr.pack(fill=X)

btn1 = Button(root, bg='#ff0000', command=redBtn)
btn2 = Button(root, bg='#ff7d00', command=orangeBtn)
btn3 = Button(root, bg='#ffff00', command=yellowBtn)
btn4 = Button(root, bg='#00ff00', command=greenBtn)
btn5 = Button(root, bg='#007dff', command=blueBtn)
btn6 = Button(root, bg='#0000ff', command=darkblueBtn)
btn7 = Button(root, bg='#7d00ff', command=violetBtn)
btn1.pack(fill=X)
btn2.pack(fill=X)
btn3.pack(fill=X)
btn4.pack(fill=X)
btn5.pack(fill=X)
btn6.pack(fill=X)
btn7.pack(fill=X)

root.mainloop()
