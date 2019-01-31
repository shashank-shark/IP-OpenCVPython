import cv2

def print_howto():
	print ("Grayscale - g")
	print ("YUV - y")
	print ("HSV - h")

if __name__ == "__main__":
	print_howto()

	cap = cv2.VideoCapture(0)

	# check if the webcam is opened correctly
	if not cap.isOpened():
		raise IOError("Cannot open webcam")

	cur_mode = None

	# start capturing frames
	while True:
		ret, frame = cap.read()
		frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

		c = cv2.waitKey(1)

		if c == 27:
			break

		if c != -1 and c != 255 and c != cur_mode:
			cur_mode = c

		if cur_mode == ord ('g'):
			output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		elif cur_mode == ord ('y'):
			output = cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
		elif cur_mode == ord ('h'):
			output = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		else:
			output = frame

		cv2.imshow('Ouput', output)

	cap.release()
	cv2.destroyAllWindows()