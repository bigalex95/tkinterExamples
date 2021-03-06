import cv2
import numpy as np

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve

# mouse callback function
line = []


def interactive_drawing(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.line(img, (ix, iy), (x, y), (0, 0, 255, 0.1), 1)
                ix = x
                iy = y
                tmp = [ix, iy, time.time()]
                line.append(tmp)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
    return x, y


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('begueradj')
cv2.setMouseCallback('begueradj', interactive_drawing)
while(1):
    cv2.imshow('begueradj', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
