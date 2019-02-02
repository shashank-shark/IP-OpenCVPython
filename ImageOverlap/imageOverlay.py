import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

face_mask = cv2.imread ('anon.jpg')
h_mask, w_mask = face_mask.shape[:2]

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classfier xml file')

cap = cv2.VideoCapture(0)

# start reading the frames
while True:
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.8, fy=0.8, 
		interpolation=cv2.INTER_AREA)

	face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

	for x,y,w,h in face_rects:
		if x<=0 or w<=0:
			pass

		h,w = int(1.07*h), int(1.0*w)
		y -= int (-0.08*h)
		x = int(x)

		# extract the region of intrest from the image
		frame_roi = frame[y:y+h, x:x+w]
		face_mask_small = cv2.resize (face_mask, (w,h), interpolation=cv2.INTER_AREA)

		# convert the color image to grayscale and threshold it
		gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
		ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)

		# create an inverse mask
		mask_inv = cv2.bitwise_not(mask)

		try:
			masked_face = cv2.bitwise_and(face_mask_small, face_mask_small,mask=mask)
			masked_frame = cv2.bitwise_and(frame_roi, frame_roi,mask=mask_inv)
		except cv2.error as e:
			print ('Ignoring arithemetic expression:' + str(e))

		# add the two images to get the final output
		frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)

	cv2.imshow('Face detector', frame)
	c = cv2.waitKey(1)
	if c == 27:
		break;

cap.release()
cv2.destroyAllWindows()