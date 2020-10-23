# https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import *

root = Tk()
root.title('My first GUI application')
root.iconphoto(True, PhotoImage(
    file='/home/alibek/Desktop/learningprojects/tkinter/tkinterExamples/lesson1/python.png'))
root.geometry('500x300+1000+500')
root.resizable(False, False)
root.config(bg='Violet')


root.mainloop()
