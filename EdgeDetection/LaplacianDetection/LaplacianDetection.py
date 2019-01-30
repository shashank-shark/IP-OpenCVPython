import cv2
import numpy as np

img = cv2.imread ('../cat2.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# It is used depth of cv2.CV_64F.
laplacian = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow ('Original', img)
cv2.imshow ('laplacian', laplacian)
cv2.imwrite('laplacian.jpg',laplacian)
print ("Very NOISY")
cv2.waitKey(0)