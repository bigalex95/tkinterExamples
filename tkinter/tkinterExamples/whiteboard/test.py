import pyautogui
import cv2
import numpy

print(pyautogui.position())  # Get current mouse position.
im1 = pyautogui.screenshot()
img = numpy.array(im1)
cv2.imshow('img', img)
pyautogui.alert(text='', title='', button='OK')
cv2.waitKey(10000)
