from __future__ import print_function
import argparse
import cv2

# create an object of argparser to read the command line arguments or image location
ap = argparse.ArgumentParser ()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# read the image here
image = cv2.imread(args["image"])

# print the height and width of the imahe
print ("Height of the image is : {} pixels".format(image.shape[0]))
print ("Width of the image is : {} pixels".format(image.shape[1]))

# print the number of channels in the image
print ("Number of channels in the image is : {} ".format(image.shape[2]))

# display the image
cv2.imshow ("Image",image)
cv2.waitKey(0)


