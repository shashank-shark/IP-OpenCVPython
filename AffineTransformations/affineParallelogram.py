import cv2
import numpy as np

img = cv2.imread ('cat3.jpg', cv2.IMREAD_COLOR)

noOfRows, noOfColumns = img.shape[:2]

# prepare the source points
src_points = np.float32 ([[0,0],[noOfColumns-1,0],[0,noOfRows-1]])

# prepare the destination points
dst_points = np.float32 ([[0,0], [int(0.6*(noOfColumns-1)),0],[int(0.4*(noOfColumns-1)),noOfRows-1]])

# generate the affine matrix
affine_matrix = cv2.getAffineTransform (src_points, dst_points)

# apply the transform
img_affineTransform = cv2.warpAffine (img, affine_matrix,(noOfColumns,noOfRows))

# disply the image
cv2.imshow ('Affine Transform image', img_affineTransform)

cv2.imwrite ('AffineTransfomed.jpg', img_affineTransform)
cv2.waitKey(0)