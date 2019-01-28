import cv2
import numpy as np

img = cv2.imread ('cat4.jpg', cv2.IMREAD_COLOR)

noOfRows, noOfColumns = img.shape[:2]

# create rotation matrix of 2-dimension
#
#	rotationMatrix = [cos@ -sin@]
#					 [sin@  cos@]
#
rotation_matrix = cv2.getRotationMatrix2D ((noOfColumns/2, noOfRows/2),30,0.7)

# rotate the image
img_rotation = cv2.warpAffine (img, rotation_matrix, (noOfColumns, noOfRows))
cv2.imshow ('Rotation', img_rotation)
cv2.imwrite ('Rotated.jpg', img_rotation)
cv2.waitKey(0)
