import cv2

image = cv2.imread('watch.jpg')
cv2.imwrite('my.jpg',image) ## Write new image from old image