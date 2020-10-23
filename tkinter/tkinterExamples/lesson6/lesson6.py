# https://www.tutorialspoint.com/python/tk_pack.htm
# https://www.tutorialspoint.com/python/tk_frame.htm
from tkinter import *

root = Tk()
root.geometry('500x500+1000+500')


# 1st Example
# f_top = Frame(root)
# f_bottom = Frame(root)
# f_top.pack()
# f_bottom.pack()

# 2nd Example
# f_top = LabelFrame(root, text='Top Frame', padx=10, pady=10)
# f_bottom = LabelFrame(root, text='Bottom Frame', padx=10, pady=10)
# f_top.pack(pady=10)
# f_bottom.pack()


# lbl1 = Label(f_top, text='1', font='15', fg='#fff',
#              bg='#3498db', width=8, height=4).pack(side=LEFT)
# lbl2 = Label(f_top, text='2', font='15', fg='#fff',
#              bg='#2ecc71', width=8, height=4).pack(side=LEFT)
# lbl3 = Label(f_bottom, text='3', font='15', fg='#fff',
#              bg='#f1c40f', width=8, height=4).pack(side=LEFT)
# lbl4 = Label(f_bottom, text='4', font='15', fg='#fff',
#              bg='#43395e', width=8, height=4).pack(side=LEFT)

lbl1 = Label(root, text='1', font='15', fg='#fff',
             bg='#3498db', width=8, height=4).pack(expand=1, anchor=S)


root.mainloop()
