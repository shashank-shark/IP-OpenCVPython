import cv2
import numpy as np

img = cv2.imread ('cat2.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# It is used depth of cv2.CV_64F.
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow ('Original', img)
cv2.imshow ('Sobel_Vertical', sobel_vertical)
cv2.imwrite('sobelVertical.jpg',sobel_vertical)
cv2.waitKey(0)