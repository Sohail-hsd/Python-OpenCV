import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

# cv.imshow('Rectangle',rectangle)
# cv.imshow('Circle',circle)

''' bitwise And '''
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('BitWise And ',bitwise_and)

''' bitwise OR '''
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('BitWise or ',bitwise_or)

''' bitwise XOR '''
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('BitWise XOR ',bitwise_xor)

''' bitwise not (Invert the Binnary colors) '''
# invert rectangle
bitwise_not_rectangle = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not Rectangle',bitwise_not_rectangle)
# Invert Cirlce
bitwise_not_cirlce = cv.bitwise_not(circle)
cv.imshow('Bitwise Not Circle',bitwise_not_cirlce)


cv.waitKey(0)


# import  cv2 as cv

# img = cv.imread('photos/4.jpg')
# cv.imshow('Image',img)


# cv.waitKey(0)
