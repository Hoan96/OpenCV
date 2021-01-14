import cv2

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cas.detectMultiScale(gray,1.2,4)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(w,h),(255,5,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()