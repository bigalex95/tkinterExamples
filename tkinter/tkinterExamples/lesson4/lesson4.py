# https://www.tutorialspoint.com/python/tk_label.htm
from tkinter import *

root = Tk()
root.geometry('500x300+1000+500')

# 1st Example
lbl = Label(
    root,
    text='Text in the row 1\nRow 2\nRow 3\n',
    bg='pink',
    fg='black',
    font=('Comic Sans MS', 10, 'bold'),
    justify=LEFT,
    width=20,
    height=10,
    anchor=E)
lbl.pack()

# 2nd Example
img = PhotoImage(
    file='/home/alibek/Desktop/learningprojects/tkinter/tkinterExamples/lesson1/python.png')
lbl_image = Label(root, image=img)
lbl_image.pack()

root.mainloop()
