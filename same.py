import cv2
import numpy as np
import matplotlib.pyplot as plt

#image = cv2.imread('watch.jpg')
#cv2.imwrite('my.jpg',image) ## Write new image from old image
#cv2.imshow('image',image) # This is show image
image = cv2.imread('watch.jpg',0) ## Have AUTOSIZE and NORMAL


img = cv2.imread('watch.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
#bytearrayd = bytearray(image)
#print(bytearrayd)
#cv2.imshow('image',image)
#cv2.waitKey(0) # this is wait anykey from user
#cv2.destroyAllWindows() # destroy all show windows
