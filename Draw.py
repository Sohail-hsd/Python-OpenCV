import cv2 as cv
import numpy as np

''' Draw a images (Blank). Paint the blank image BGR(blue,green,red) '''
# Create a blank image.
blank = np.zeros((500, 500, 3), dtype='uint8')


def DrawColorImages():
    blank_image = np.zeros((500, 500, 3), dtype='uint8')
    # This will create a blank image of shape, 500 by 500, of 3 channels.
    cv.imshow('blank', blank_image)

    ''' Paint image (Blue, Green, Red)'''
    # Take the balnk image and refrences all the pixcel by (balnk[:]), this will refrences all the pixcel
    blank_image[:] = 0, 255, 0
    # Then we can set the pixcel color values (RGB) formatt.
    cv.imshow('Green', blank_image)

    blank_image[:] = 255, 0, 0
    cv.imshow('Blue', blank_image)

    blank_image[:] = 0, 0, 255
    cv.imshow('Red', blank_image)

    cv.waitKey(0)


''' Pick a range of pixels and color them. '''


def ColorSpecificPortion():
    # Pick a range of pixels and color them only.
    blank[50:100, 100:150] = 255, 0, 0
    blank[150:200, 200:250] = 0, 255, 0
    blank[250:300, 300:350] = 0, 0, 255
    cv.imshow('color_Secific_Portion', blank)
    cv.waitKey(0)


# we can get the center of the image by (img.shape[1]//2, img.shape[0]//2)

''' Draw a ractanges on a blank image. '''
# cv.rectangle(blank,(0,0),(250,250), (0,255,255), thickness=2)
# This finction will take an Image, (point1) (point2) ( BGR Color) and thinkness and line type (Optional).
# if you want to fill the rectangel, just pass the (thinkness= cv.FILLED) or just pass the -1.
# cv.imshow('Rectangel',blank)

''' Draw a Circle on a blank image '''
# cv.circle(blank, (255, 255), 40, (255, 255, 0), thickness=3)
# # this will take an Image,
# # cv.imshow('Circle', blank)

# #       img    p1      p2                                  color        thickness
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,255), thickness=3)
# cv.imshow('Line',blank)

''' Draw a TEXT on a blank image '''
cv.putText(blank,"The Text on Image",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,200,100),2)
cv.imshow("Text_on_Image",blank)

cv.waitKey(0)
# ColorSpecificPortion()
# DrawColorImages()
