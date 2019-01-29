import cv2
import numpy as np
import math

img = cv2.imread ('cat4.jpg',cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# creating a vertical wave
img_output = np.zeros (img.shape, dtype=img.dtype)


for i in range (rows):
	for j in range (cols):
		offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
		offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
		if i+offset_y < rows and j+offset_x < cols:
			img_output [i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
		else:
			img_output[i,j] = 0

cv2.imshow ('Output', img_output)
cv2.imwrite ('HorizontalVerticalWrap.jpg', img_output)
cv2.waitKey(0)
