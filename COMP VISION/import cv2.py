import cv2
# path
path = r'C:\COMP VISION\Princess m.jpg'
# Using cv2.imread() method
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# Displaying the image
cv2.imshow('MY first computer Vision Program', img)
cv2.waitKey(0)