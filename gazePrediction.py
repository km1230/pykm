import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


"""
cascade classifier from Haar Cascade data for facial and eye detection
"""
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')


"""
machine learning from collected data 'gaze.txt'
"""
data = pd.read_csv('gaze.txt', 
	names=['centre', 'radius', 
		'face_x', 'face_y','face_w','face_h',
		'eye_x', 'eye_y','eye_w','eye_h',
		'gaze']
		)
x = data.drop('gaze', axis=1)
y = data['gaze']
#rfc = RandomForestClassifier()
#rfc.fit(x, y)
tree = DecisionTreeClassifier()
tree.fit(x, y)


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


			"""
			detect pupil
			"""
			circles = cv2.HoughCircles(roi_gray,cv2.HOUGH_GRADIENT,1,60,param1=200,param2=10,minRadius=9,maxRadius=20)
			
			"""
			draw circle - pupil
			"""
			x_test = np.array([])
			count = 0
			if circles is not None:
				for i in circles[0, :]:
					if (
						(i[0] >= ex) and 
						(i[0] <= end_cord_ex) and 
						(i[0] >= ey) and 
						(i[0] <= end_cord_ey) and
						(end_cord_ey <=end_cord_y/2) and
						(ew < 100) and
						(eh < 100)
						):
						cv2.circle(roi_color, (i[0], i[1]), i[2], (255,255,255), 2)
						cv2.circle(roi_color, (i[0], i[1]), 2, (0,0,255), 3)
						

						"""
						Gaze prediction from the Decision Tree Model (machine learning)
						"""
						track = np.array([i[0], i[1], x, y, w, h, ex, ey, ew, eh])
						print(('track:{}').format(track))
						print(tree.predict([track]))					
						


	#display the frames
	cv2.imshow('Face Recognition', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release
cv2.destroyAllWindows()
