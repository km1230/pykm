import numpy as np
import cv2

cap = cv2.VideoCapture(0) #device number or video file


"""
>>>>set resolution
>>>>cap.set(propID, double)
"""
cap.set(3, 1920)
cap.set(4, 1080)


"""
>>>>resize captured frame
>>>>.shape() returns the dimension of captured images in tuple
	(rows, cols, channels for color e.g. 3)
>>>>cv2.resize(image, (width, height), interpolation method)
"""
def scaling(frame, percent):
	width = int(round(frame.shape[1] * percent/100))
	height = int(round(frame.shape[0] * percent/100))
	newDimension = (width, height)
	return cv2.resize(frame, newDimension, interpolation=cv2.INTER_LINEAR)


p = int(input('scale in % (50-100): '))

while True:
	ret, frame = cap.read()


	#convert color
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	newFrame = scaling(gray, p)
	
	cv2.imshow('frame', newFrame) #show the images


	"""
	>>>>waitKey->delay in ms, waitKey(0)->forever
	>>>>0xFF <hex> = 11111111 <binary>, i.e. to detect the last 8 bits of waitKey() only 
		regardless of on/off NumLock
		<https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1>
	>>>>if 'q' <ASCII value> is hit after 25ms->break
	"""
	if cv2.waitKey(25) & 0xFF == ord('q'): 
		break

cap.release()
cv2.destroyAllWindows()