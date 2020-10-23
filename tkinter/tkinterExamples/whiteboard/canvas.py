import tkinter as tk
import time
from PIL import Image, ImageDraw, ImageFont, ImageTk


lastx, lasty = 0, 0
line = []


def clearCanvas(event):

    while line:
        canvas.delete('all')
        pX = line[0][0]
        pY = line[0][1]
        for i in range(len(line)):
            alpha = time.time() - line[i][2]
            alpha = int(255 - alpha*80)
            # print(alpha)
            #canvas.create_line(pX, pY, line[i][0], line[i][1], alpha=alpha)
            draw.line([(pX, pY), (line[i][0], line[i][1])],
                      fill=(255, 0, 255, alpha), width=15)


def xy(event):
    "Takes the coordinates of the mouse when you click the mouse"
    global lastx, lasty
    lastx, lasty = event.x, event.y


def addLine(event):
    """Creates a line when you drag the mouse
    from the point where you clicked the mouse to where the mouse is now"""
    global lastx, lasty, line
    canvas.create_line(lastx, lasty, event.x, event.y)
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y
    tmp = [lastx, lasty, time.time()]
    line.append(tmp)


root = tk.Tk()
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = tk.Canvas(root)
pano = Image.new("RGBA", (800, 600), (255, 255, 255, 255))
draw = ImageDraw.Draw(pano)
panoTK = ImageTk.PhotoImage(pano)
canvas.create_image(0, 0, anchor=tk.NW, image=panoTK)
canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind('<ButtonRelease-1>', clearCanvas)

root.mainloop()
