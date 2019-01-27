import cv2

# read the image im COLOR space
img = cv2.imread ('cat2.jpg', cv2.IMREAD_COLOR)

# convert the color image to grayscale
gray_scale_image = cv2.cvtColor (img, cv2.COLOR_RGB2GRAY)

# display the image
cv2.imshow ("Gray Cat",gray_scale_image)

# save the image
catGray = cv2.imwrite ("Graycat.jpg", gray_scale_image)

cv2.waitKey (0)