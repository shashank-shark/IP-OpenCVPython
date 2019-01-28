import cv2
import numpy as np

img = cv2.imread ('cat5.jpg', cv2.IMREAD_COLOR)

numOfRows, numOfColumns = img.shape[:2]

# create the translation matrix
# the translation matrix can be defined as below
#						[1 0 Tx]
#	translationMatrix = [0 1 Ty]
#	here Tx = 70 and Ty = 110 (say)					
translation_matrix = np.float32 ([[1,0,70],[0,1,110]])

# translation of image
img_translation = cv2.warpAffine (img, translation_matrix, (numOfColumns, numOfRows), cv2.INTER_LINEAR)

cv2.imshow ('Image Translation', img_translation)
cv2.waitKey(0)

