# https://prnt.sc/oo53q6
from tkinter import *

root = Tk()
# root.geometry('500x300+1000+500')

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


class MyButtons:
    def __init__(self, master, text_color, hex_color):
        super().__init__()
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(master, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        ntr.delete(0, END)
        ntr.insert(0, self.hex_color)
        lbl['text'] = self.text_color
        lbl['fg'] = self.hex_color


for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()
