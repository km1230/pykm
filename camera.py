import numpy as np
import cv2

"""
>>>>some parameters to be used for video recording
"""
filename = 'video.avi'
fps = 20.0 #fit macbook pro media output
dimension = (1280,720)
fourcc = cv2.VideoWriter_fourcc(*'avc1')



"""
>>>>resize captured video
>>>>.shape returns the dimension of captured images in tuple
	(rows, cols, channels for color e.g. 3)
>>>>cv2.resize(image, (width, height), interpolation method)

def scaling(frame, percent):
	width = int(round(frame.shape[1] * percent/100))
	height = int(round(frame.shape[0] * percent/100))
	newDimension = (width, height)
	return cv2.resize(frame, newDimension, interpolation=cv2.INTER_LINEAR)

p = int(input('scale in % (50-100): '))
"""


"""
>>>>device number or video file
"""
cap = cv2.VideoCapture(0)


"""
>>>>set resolution
>>>>cap.set(propID, double)
"""
cap.set(3, dimension[0])
cap.set(4, dimension[1])


"""
>>>>output recorded video
"""
out = cv2.VideoWriter(filename, fourcc, fps, dimension, True)

while True:
	ret, frame = cap.read()


	"""
	>>>>convert color

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	"""


	"""
	>>>>a self defined function for resizing the frame
	
	newFrame = scaling(gray, p)
	"""
	

	"""
	>>>>save captured video and write file
	"""
	if ret:
		out.write(frame)


		"""
		>>>>show video captured
		"""
		cv2.imshow('frame', frame)


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
out.release()
cv2.destroyAllWindows()