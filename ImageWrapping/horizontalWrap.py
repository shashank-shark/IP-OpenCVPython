import cv2
import numpy as np
import math

img = cv2.imread ('cat4.jpg',cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# creating a vertical wave
img_output = np.zeros (img.shape, dtype=img.dtype)


for i in range (rows):
	for j in range (cols):
		offset_y = int (16.0 * math.sin (2*3.14*j/180))
		offset_x = 0

		if i + offset_y < rows:
			img_output[i,j] = img[(i+offset_y)%rows,j]
		else:
			img_output[i,j] = 0

cv2.imshow ('Output', img_output)
cv2.imwrite ('HorizontalWrap.jpg', img_output)
cv2.waitKey(0)
