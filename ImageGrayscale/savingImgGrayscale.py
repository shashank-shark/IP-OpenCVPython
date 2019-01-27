import cv2

# read the image in grayscale
grayImage = cv2.imread ('cat1.jpg', cv2.IMREAD_GRAYSCALE)

# show the image
cv2.imshow ('Grayscale', grayImage)

# save the grayscale image
cv2.imwrite ('Grayscalecat.jpg', grayImage)

# wait for the quit action stroke
cv2.waitKey(0)