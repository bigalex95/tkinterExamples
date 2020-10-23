import cv2

image = cv2.imread('test.jpeg')
overlay = image.copy()

x, y, w, h = 10, 10, 100, 100  # Rectangle parameters
cv2.line(overlay, (x, y),
         (x+w, y+h), (255, 0, 0), 10)

alpha = 0.3  # Transparency factor.

# Following line overlays transparent rectangle over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.line(overlay, (x+w, y),
         (x, y+h), (255, 255, 0), 10)
# Following line overlays transparent rectangle over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.imshow('Alpha', image_new)
cv2.waitKey(10000)
