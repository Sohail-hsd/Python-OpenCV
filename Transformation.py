import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpg')
# cv.imshow('Img',img)

''' Transcaltion is shifting the images along the (x,y) axis. we cna shift img (up,down,right,below) '''


def translate(img, x, y):
    ''' To translate a image we first create an translation matrix. and then diminsion of the images'''
    ''' this matrix will be a list of two lists.[[][]] '''
    ''' This function will return an  Tresformation image. '''
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, dimension)


''' -x ---> Left '''
''' -y ---> Up '''
''' x ---> Right '''
''' y ---> Down '''

transimg = translate(img, 100, 100)
# cv.imshow('Translate', transimg)

''' Rotation '''


def rotate(img, angle, roPoint=None):
    ''' Extracting height and width from img '''
    ''' If the rotating point None then make it center of the img. '''
    ''' Make a rotating Matrix with (rotatePoint,angle,scale) '''
    ''' Get the diminsion of the img. '''
    ''' return the img by cv.WarpAffine(img,rotating_matrix, diminsion) '''
    (height, width) = img.shape[:2]

    if(roPoint is None):
        roPoint = (width//2, height//2)

    rotate_Matirx = cv.getRotationMatrix2D(roPoint, angle, 1.0)
    diminsion = (width, height)
    return cv.warpAffine(img, rotate_Matirx, diminsion)

# rotated = rotate(img,90)
# cv.imshow("Rotated",rotated)

''' Flip the image '''
# flip code (0,1,-1) 
# 0 means flip Verically, 1 means filp Horizantilly, -1 means filp both vertically and horizanlly
fliped = cv.flip(img,0)
cv.imshow('Fliped Vertically',fliped)
fliped = cv.flip(img,1)
cv.imshow('Fliped Horizantally',fliped)
fliped = cv.flip(img,-1)
cv.imshow('Fliped Both (Y and X)',fliped)

cv.waitKey(0)
