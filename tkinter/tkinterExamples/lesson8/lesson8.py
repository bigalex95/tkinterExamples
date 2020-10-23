# https://www.tutorialspoint.com/python/tk_place.htm
from tkinter import *

root = Tk()

# 1st Example
# lbl1 = Label(root, text='Hello World!', bg='#3498db',
#              fg='#fff', font='16', padx=20, pady=8)
# lbl1.place(x=0, y=0)

# lbl2 = Label(root, text='Hello World!', bg='#3498db',
#              fg='#fff', font='16', padx=20, pady=8)
# lbl2.place(relx=0.5, rely=0.5, anchor=CENTER)

# 2nd Example
# btn1 = Button(root, text='Button 1', bg='#3498db',
#               fg='#fff', font='16', padx=20, pady=8)
# btn1.place(x=0, y=0)

# btn2 = Button(root, text='Button 2', bg='#2ecc71',
#               fg='#fff', font='16', padx=20, pady=8)
# btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

# btn3 = Button(root, text='Button 3', bg='#f1c40f',
#               fg='#fff', font='16', padx=20, pady=8)
# btn3.place(relx=1, rely=1, anchor=SE)

# 3rd Example
lbl = Label(root, bg='black')
lbl.place(relheight=0.7, relwidth=0.7, relx=0.15, rely=0.15)

btn2 = Button(root, text='Button 2', bg='#2ecc71',
              fg='#fff', font='16', padx=20, pady=8)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
