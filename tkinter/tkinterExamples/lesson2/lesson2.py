# https://www.tutorialspoint.com/python/tk_button.htm
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('500x300+1000+500')

# btn2 = ttk.Button(root, text='Button2')
# btn2.pack()
# Button(root, text='Button').pack()


def clicked():
    messagebox.showinfo('Clicked', 'Button clicked!')


# btn = Button(root, text='Button', command=clicked,
#              width=10, font=('Comic Sans MS', 20, 'bold'))
# btn.pack()
btn = Button(root, text='Button 1\n22', justify=LEFT)
btn.config(width=20, height=5)
# btn['font'] = 'Arial 15 bold'
# btn['command'] = clicked
btn.pack()


root.mainloop()
