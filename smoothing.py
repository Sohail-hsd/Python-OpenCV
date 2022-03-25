import  cv2 as cv

img = cv.imread('photos/8.jpg')
cv.imshow('Image',img)

''' Average blur '''
average_blur = cv.blur(img,(3,3))
cv.imshow('Average Blur',average_blur)

''' Gaussian blur '''

gussain_blur = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gussain Blur',gussain_blur)

''' Median Blur (More effective on removing some Noises in the images)  '''
median_blur = cv.medianBlur(img,3)
cv.imshow('Median Blur',median_blur)

''' Bilateral Blur (Most Effective in advance projects) '''
# this take img, diameter, sigmaColor, sgmaSpace.
bilateral_blur = cv.bilateralFilter(img,15,35,25)
cv.imshow('Bilateral Blur',bilateral_blur)

cv.waitKey(0)


# import  cv2 as cv

# img = cv.imread('photos/4.jpg')
# cv.imshow('Image',img)



# cv.waitKey(0)