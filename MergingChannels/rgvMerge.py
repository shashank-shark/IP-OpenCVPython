import cv2

img = cv2.imread ('cat6.jpg', cv2.IMREAD_COLOR)

g,b,r = cv2.split (img)

# GBR merging
gbrImage = cv2.merge ((g,b,r))

# RBR merging
rbrImage = cv2.merge ((r,b,r))

# BRB merging
brbImage = cv2.merge ((b,r,b))

# GBR MERGING
gbgImage = cv2.merge ((g,b,g))

# RGR merging
rgrImage = cv2.merge ((r,g,r))

# GRG
grgImage = cv2.merge ((g,r,g))

# display the images
cv2.imshow ('Original', img)
cv2.imshow ('GBR MERGING', gbrImage)
cv2.imshow ('RBR MERGING', rbrImage)
cv2.imshow ('BRB MERGING', brbImage)
cv2.imshow ('GBG MERGING', gbgImage)
cv2.imshow ('RGR MERGING', rgrImage)
cv2.imshow ('GRG MERGING', grgImage)

# save the different color spaces
cv2.imwrite ('GBRMerge.jpg',gbrImage)
cv2.imwrite ('RBRMerging.jpg', rbrImage)
cv2.imwrite ('BRBMerging.jpg', brbImage)
cv2.imwrite ('GBGMerging.jpg', gbgImage)
cv2.imwrite ('RGRImage.jpg', rbrImage)
cv2.imwrite ('GRGImage.jpg', grgImage)

cv2.waitKey (0)