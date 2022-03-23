import cv2 as cv

'''Reading Images'''

img = cv.imread('photos/6re.jpg')
cv.imshow('NFT',img)
cv.waitKey(0)