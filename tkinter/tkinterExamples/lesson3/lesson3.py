# https://www.tutorialspoint.com/python/tk_button.htm
from tkinter import *
import time

root = Tk()
root.geometry('500x300+1000+500')


# 1st Example
def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')
    print(time.strftime('%H:%M:%S'))


btn_time = Button(root, text='Check Time', command=check_time)
btn_time.pack()


# 2nd Example
root.title('Counter')
clicks = 0


def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')


btn_cnt = Button(root, text='Counter', command=counter)
btn_cnt.pack()


root.mainloop()
