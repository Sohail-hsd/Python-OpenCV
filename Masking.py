import cv2 as cv
import numpy as np

''' Masking allow us to focus on certain part of image. (Example : Mask over the peoples faces in an image) '''

img = cv.imread('photos/4.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
center = (img.shape[1]//2, img.shape[0]//2)
# circle = cv.circle(blank, center, 200, 255, -1)
rectangle = cv.rectangle(blank,(30,30),(370,370),255,-1)
# cv.imshow('Circle', circle)
cv.imshow('Rectangle', rectangle)

bitwise_and = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Bitwise Circle AND', bitwise_and)

cv.waitKey(0)
