import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#define to the save object
foyrcc = cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('hihi.avi',foyrcc,20.0,(640,480))

while (True):
	ret,frame = cap.read() # capture to ret and frame
	if ret == True:
		frame = cv2.flip(frame,0)

		#out.write(frame)

		cv2.imshow('frame',frame)

		if cv2.waitKey(1) & 0xFF == ord('x'):
			break
	else:
		break
	#Convert frame to gray
	#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#show video
	#cv2.imshow('frame',gray)
	#any key x to break while
	#if cv2.waitKey(1) & 0xFF== ord('x'):
	#	break
cap.release()
out.release()
cv2.destroyAllWindow()