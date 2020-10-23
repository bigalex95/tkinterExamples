# https://www.tutorialspoint.com/python/tk_entry.htm
from tkinter import *

root = Tk()
root.geometry('500x300+1000+500')


def add_str():
    ntr.insert(END, 'Hello!')


def del_str():
    ntr.delete(0, END)


def get_str():
    lbl_text['text'] = ntr.get()


lbl = Label(root, text='Entry area')
lbl.pack()

ntr = Entry(root)
# ntr = Entry(root, show='*')
ntr.pack()

btn_add = Button(root, text='Add', command=add_str)
btn_del = Button(root, text='Delete', command=del_str)
btn_get = Button(root, text='Get', command=get_str)
btn_add.pack()
btn_del.pack()
btn_get.pack()

lbl_text = Label(root, bg='blue', fg='red')
lbl_text.pack(fill=X)

root.mainloop()
