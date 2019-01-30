import cv2
import numpy as np

img = cv2.imread('../cat1.jpg', 0)

# equalize the histogram of the input image
histeq = cv2.equalizeHist(img)

cv2.imshow('Input', img)
cv2.imshow('Histogram equalized', histeq)
cv2.imwrite('Contrast.jpg', histeq)
cv2.waitKey(0)