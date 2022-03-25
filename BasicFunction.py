import cv2 as cv

img = cv.imread('photos/6re.jpg')

# cv.imshow('image',img)

''' Converting image to grascale '''
# cv.cvtColor() is use to convert images to (grayscale, etc)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

''' Blur an image '''
# cv.GaussianBlur (Source, kernalSize ) the kernal must be a tuple of ODD.
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

''' Edge Cascade, use to find edges in the images '''
# cv.Canny will take image and 2 threshold values. we can reduce the edges by bluring the images.
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny',canny)

''' Dilating the images  '''
# this will take a canny image and dilate it
dilated = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow('Dilated',dilated)

''' Eroding an image '''
# this will take a dialated image and erode the image
erode = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Erode',erode)

'''' Resize an image, with reize function '''
# this will take an image and distination size. (the resized value). and interpolation( usefull when shrinking the image)
resize = cv.resize(img,(400,400), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize',resize)

''' Crop an image '''
''' Images are arrays, so we can apply some arrays sclicing (on the basis of pixel values) '''
# we can select a regin of pixels img[heigt,width]
croped = img[10:200,200:700]
cv.imshow('Croped',croped)

cv.waitKey(0)
