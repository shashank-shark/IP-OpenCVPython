import cv2

img = cv2.imread ('cat5.jpg', cv2.IMREAD_COLOR)

# convert the image into yuv-format
yuv_image = cv2.cvtColor (img, cv2.COLOR_BGR2YUV)

# Splitting the color image into y , u , v channels
yChannel, uChannel, vChannel = cv2.split (yuv_image)

# disply each image with external Splitting
cv2.imwrite ('YChannel.jpg', yuv_image[:,:,0])
cv2.imshow ('Y channel', yuv_image[:,:,0])
cv2.imwrite ('UChannel.jpg', yuv_image[:,:,1])
cv2.imshow ('U channel', yuv_image[:,:,1])
cv2.imwrite ('VChannel.jpg', yuv_image[:,:,2])
cv2.imshow ('V channel', yuv_image[:,:,2])

cv2.waitKey(0)