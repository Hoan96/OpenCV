import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

print(cap.isOpened())
while  (cap.isOpened()):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('hihi',gray)

    if cv2.waitKey(1) & 0xFF == ord ('x'):
        break
cap.release()
cv2.destroyAllWindows()