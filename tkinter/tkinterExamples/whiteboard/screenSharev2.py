import time

import cv2
import mss
import numpy

from PIL import Image, ImageDraw, ImageFont

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve

# mouse callback function
line = []


def interactive_drawing(event, x, y, flags, param):
    global ix, iy, drawing, mode, line

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                ix = x
                iy = y
                tmp = [ix, iy, time.time()]
                line.append(tmp)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        line.append([-1, -1, time.time()])
    return x, y


screen = True
with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 0, "left": 0, "width": 1366, "height": 768}
    cv2.namedWindow('OpenCV/Numpy normal', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('OpenCV/Numpy normal',
                          cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('OpenCV/Numpy normal', interactive_drawing)
    # Get raw pixels from the screen, save it to a Numpy array
    img = numpy.array(sct.grab(monitor))
    base = Image.fromarray(img).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    while screen:
        last_time = time.time()

        if line:
            pX = line[0][0]
            pY = line[0][1]
            for i in range(len(line)):
                alpha = time.time() - line[i][2]
                alpha = int(255 - alpha*80)
                #print(alpha)
                if line[i][0] != -1:
                    draw.line([(pX, pY), (line[i][0], line[i][1])], fill=(255, 0, 255, alpha), width=15)
                    #cv2.line(img, (pX, pY),
                    #         (line[i][0], line[i][1]), (0, 0, 255), 1)
                    pX = line[i][0]
                    pY = line[i][1]
                else:
                    if i+1 < len(line):
                        pX = line[i+1][0]
                        pY = line[i+1][1]

        # Display the picture
        out = Image.alpha_composite(base, txt)
        img_final = numpy.array(out)
        cv2.imshow("OpenCV/Numpy normal", img_final)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        ##print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
