import cv2
import numpy as np

img = cv2.imread ('cat5.jpg')

rows, cols = img.shape[:2]

# creating kernel
#		[0 0 0]
#	K =	[0 1 0]
#		[0 0 0]

kernel_identity = np.array ([[0,0,0],[0,1,0],[0,0,0]])

kernel_3x3 = np.ones ((3,3), np.float32) / 9.0

kernel_5x5 = np.ones ((5,5), np.float32) / 25.0

# show the original image
cv2.imshow ('Original Image', img)

# apply and display the identity kernel
identity_img = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow ('IdentityKernelBlur.jpg', identity_img)
cv2.imwrite ('IdentityKernelBlur.jpg', identity_img)

# apply and display kernel_3x3
kernel_3x3_img = cv2.filter2D (img, -1, kernel_3x3)
cv2.imshow ('3x3KernelBlur.jpg', kernel_3x3_img)
cv2.imwrite ('3x3KernelBlur.jpg', kernel_3x3_img)

# apply and display kernel_5x5
kernel_5x5_img = cv2.filter2D (img, -1, kernel_3x3)
cv2.imshow ('5x5KernelBlur.jpg', kernel_5x5_img)
cv2.imwrite ('5x5KernelBlur.jpg', kernel_3x3_img)

cv2.waitKey(0)