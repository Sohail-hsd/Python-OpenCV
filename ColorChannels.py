import cv2 as cv
import numpy as np

img = cv.imread('photos/5.jpg')

cv.imshow('Image',img)

''' Take BGR image and split it into 3 color channels (B,G,R) '''
# This will split the image into color channels (3 color chennels)
b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2],dtype='uint8')

''' display image with one channel '''
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

''' Merged the 3 color channels  '''
merged = cv.merge([b,g,r])

''' display one channels '''
# cv.imshow('B',b)
# cv.imshow('G',g)
# cv.imshow('R',r)

cv.imshow('Blur',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
cv.imshow('Mearged image',merged)


print('Img  ',img.shape)
print('Blue ',b.shape)
print('Green',g.shape)
print('Red  ',r.shape)

cv.waitKey(0)