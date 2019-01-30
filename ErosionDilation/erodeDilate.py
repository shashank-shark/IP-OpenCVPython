import cv2
import numpy as np

img = cv2.imread ('cat4.jpg',0)

# create the kernel
kernel = np.ones ((5,5), np.uint8)

img_erosion = cv2.erode (img,kernel, iterations=1)
img_dilation = cv2.dilate (img,kernel,iterations=1)

cv2.imshow ('ImgEROSION',img_erosion)
cv2.imwrite ('imgerosion.jpg',img_erosion)

cv2.imshow ('ImgDilation', img_dilation)
cv2.imwrite ('imgdilation.jpg',img_dilation)


cv2.waitKey(0)