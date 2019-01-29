import cv2
import numpy as np

img = cv2.imread('cat5.jpg')
cv2.imshow('Original', img)

kernel_sharpen_gaussian = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]]) / 8.0

output_gaussian = cv2.filter2D(img, -1, kernel_sharpen_gaussian)

cv2.imshow ('Gaussian Sharpening', output_gaussian)
cv2.imwrite ('GaussinSharpening.jpg', output_gaussian)

cv2.waitKey(0)