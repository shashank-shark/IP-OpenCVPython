import cv2
import numpy as np

img = cv2.imread ('../cat2.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# It is used depth of cv2.CV_64F.
canny = cv2.Canny(img, 50, 240)

cv2.imshow ('Original', img)
cv2.imshow ('canny', canny)
cv2.imwrite('canny.jpg',canny)
print ("CLEAR - double directional derivative")
cv2.waitKey(0)