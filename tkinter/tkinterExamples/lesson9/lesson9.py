# https://www.tutorialspoint.com/python/tk_text.htm
# https://www.tutorialspoint.com/python/tk_menu.htm
# https://www.tutorialspoint.com/python/tk_scrollbar.htm
# https://www.tutorialspoint.com/python/tk_frame.htm
from tkinter import *

root = Tk()
root.geometry('500x300+1000+300')

frm_menu = Frame(root, bg='#1f252a', height=40)
frm_text = Frame(root)
frm_menu.pack(fill=X)
frm_text.pack(fill=BOTH, expand=1)

lbl_menu = Label(frm_menu, text='Menu', bg='#2b3239',
                 fg='#c6dec1', font='Arial 10')
lbl_menu.place(x=10, y=10)

txt = Text(frm_text, bg='#343d46', fg='#c6dec1', padx=10, pady=10,
           wrap=WORD, insertbackground='#eda756', selectbackground='#4e5a65', spacing3=10, width=30)
txt.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(frm_text, command=txt.yview)
scroll.pack(fill=Y, side=LEFT)
txt.config(yscrollcommand=scroll.set)

root.mainloop()
