import cv2 as cv
import numpy as np

''' Contous are basically the boundries of objects.( the line ouccre along the boundry of the objects) '''
img = cv.imread('photos/7.jpg')
# cv.imshow("image",img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

''' Threashold, Binirize the image (if the binary in the image is zero it will be black else white) '''
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)

contorus, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{contorus} found...!')

''' To draw those controus on a blank image'''

blank = np.zeros(img.shape,dtype='uint8')

cv.drawContours(blank,contorus,-1,(0,255,0),1)
cv.imshow('Controus on blank image',blank)



cv.waitKey(0)