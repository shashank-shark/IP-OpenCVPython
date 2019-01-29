import cv2
import numpy as np

img = cv2.imread ('cat5.jpg')
cv2.imshow ('Original', img)

size = 15

# generate kernels
kernel_motion_blur = np.zeros((size,size))
kernel_motion_blur[int ((size-1)/2),:] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the image
outputImg = cv2.filter2D (img, -1, kernel_motion_blur)

cv2.imshow ('MotionBlur.jpg', outputImg)
cv2.imwrite ('MotionBlur.jpg', outputImg)

cv2.waitKey(0)