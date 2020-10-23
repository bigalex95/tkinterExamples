# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_frame.htm
from tkinter import *

root = Tk()

# frm = Frame(root)
# frm.pack(pady=10)

# 1st Example
# btn7 = Button(frm, text='7', padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(frm, text='8', padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(frm, text='9', padx=10, pady=5).grid(row=0, column=2)
# btn4 = Button(frm, text='4', padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(frm, text='5', padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(frm, text='6', padx=10, pady=5).grid(row=1, column=2)
# btn1 = Button(frm, text='1', padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(frm, text='2', padx=10, pady=5).grid(row=2, column=1)
# btn3 = Button(frm, text='3', padx=10, pady=5).grid(row=2, column=2)
# btn0 = Button(frm, text='0', padx=10, pady=5).grid(
#     row=3, column=0, columnspan=3)

# #2nd Example
# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0'
# ]

# row = 0
# column = 0

# for i in btn_list:
#     if i == '0':
#         Button(frm, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(frm, text=i, padx=10, pady=5).grid(row=row, column=column)
#     column += 1
#     if column == 3:
#         column = 0
#         row += 1

# 3rd Example
lbl_user = Label(root, text='Login:').grid(
    row=0, column=0, padx=10, pady=10, sticky=E)
ntr = Entry(root).grid(row=0, column=1, padx=10, columnspan=2, sticky=W+E)
lbl_pasword = Label(root, text='Password:').grid(
    row=1, column=0, padx=10, pady=10, sticky=E)
ntr = Entry(root).grid(row=1, column=1, padx=10, columnspan=2, sticky=W+E)

btn_login = Button(root, text='Login', padx=5).grid(
    row=2, column=0, pady=10, padx=10, sticky=E)
btn_reg = Button(root, text='Register', padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text='Forgot Password?',
                    padx=5).grid(row=2, column=2, padx=10)

root.mainloop()
