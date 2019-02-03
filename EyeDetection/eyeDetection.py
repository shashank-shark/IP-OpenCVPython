import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier file')

if eye_cascade.empty():
	raise IOError('Unable to load the eye cascade classifier file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
	ret, frame = cap.read()

	# resize the frame
	frame = cv2.resize(frame, None, fx=1.5,fy=1.5, interpolation=cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale (gray, scaleFactor=1.3,minNeighbors=3)

	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h,x:x+w];
		roi_color = frame[y:y+h,x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)

		for (x_eyes,y_eyes,w_eyes,h_eyes) in eyes:
			center = (int(x_eyes + 0.5*w_eyes),int(y_eyes + 0.5*h_eyes))
			radius = int (0.3 * (w_eyes + h_eyes))
			color = (0,0,255)
			thickness = 2
			cv2.circle(roi_color, center, radius, color, thickness)

	cv2.imshow('Eye Detector', frame)

	c = cv2.waitKey(1)
	if c == 27:
		break

cap.release()
cv2.destroyAllWindows()