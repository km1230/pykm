import numpy as np
import cv2

"""
cascade classifier from Haar Cascade data for facial and eye detection
"""
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

"""
initialize cv2 video capture object
"""
cap = cv2.VideoCapture(0)

while(True):
	"""
	capture frame
	"""
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	"""
	detect a series of real-time faces
	"""
	faces = face_cascade.detectMultiScale(gray)
	for (x, y, w, h) in faces:
		roi_gray = gray[y:y+h, x:x+w] #region of interest - gray
		roi_color = frame[y:y+h, x:x+w] #region of interest - color


		"""
		draw rectangle - face
		"""
		end_cord_x = x+w #right bottom x
		end_cord_y = y+h #right bottom y
		color = (255, 0, 0) #BGR
		stroke = 2 #thickness of border
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)


		"""
		detect a series of eyes
		"""
		eyes = eye_cascade.detectMultiScale(roi_gray)


		for (ex, ey, ew, eh) in eyes:

			"""
			draw rectangle - eyes
			"""
			end_cord_ex = ex+ew #right bottom x
			end_cord_ey = ey+eh #right bottom y
			color_eye = (0, 255, 0) #BGR
			stroke_eye = 2 #thickness of border
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), color_eye, stroke_eye)


	#display the frames
	cv2.imshow('Face Recognition', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
