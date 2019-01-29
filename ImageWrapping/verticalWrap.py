import cv2
import numpy as np
import math

img = cv2.imread ('cat4.jpg',cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# creating a vertical wave
img_output = np.zeros (img.shape, dtype=img.dtype)


for i in range (rows):
	for j in range (cols):
		offset_x = int (25.0 * math.sin (2*3.14*i/180))
		offset_y = 0

		if j + offset_x < rows:
			img_output[i,j] = img[i,(j+offset_x)%cols]
		else:
			img_output[i,j] = 0

cv2.imshow ('Output', img_output)
cv2.imwrite ('VerticlWrap.jpg', img_output)
cv2.waitKey(0)
