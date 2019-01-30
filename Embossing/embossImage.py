import cv2
import numpy as np

img = cv2.imread ('cat6.jpg')

# generating kernels
kernel_1_emboss = np.array([[0,-1,-1],[1,0,-1],[1,1,0]]) #South West
kernel_2_emboss = np.array([[-1,-1,0],[-1,0,1],[0,1,1]]) #South East
kernel_3_emboss = np.array([[1,0,0],[0,0,0],[0,0,-1]]) #North West

# converting the image to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# applying the kernels to the images
output1 = cv2.filter2D(gray_img, -1, kernel_1_emboss) + 128
output2 = cv2.filter2D(gray_img, -1, kernel_2_emboss) + 128
output3 = cv2.filter2D(gray_img, -1, kernel_3_emboss) + 128

cv2.imshow ('Embossing South-West', output1)
cv2.imwrite ('E-SW.jpg',output1)

cv2.imshow ('Embossing South-East', output2)
cv2.imwrite ('E-SE.jpg',output2)

cv2.imshow ('Embossing North West', output3)
cv2.imwrite ('E-NW.jpg',output3)

cv2.waitKey(0)