import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread('photos/7.jpg')
cv.imshow("image",img)

''' Converting BGR 2 GRAY '''

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

''' Converting BGR 2 HSV '''
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

''' Converting BGR 2 LAB '''
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB',lab)

''' Threshold '''

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)

''' Converting BGR 2 RGB '''
''' OpenCv open image in BGR fromat '''
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
