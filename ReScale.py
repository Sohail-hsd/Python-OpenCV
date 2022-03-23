from configparser import InterpolationDepthError
from sre_constants import BRANCH
from turtle import width
import cv2 as cv
from cv2 import imshow

'''Resizing and ReScaling Videos'''


def reSclaeFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    # Tupe of height and width
    dimenstion = (width, height)
    # this will return the resized frame.
    # cv.resize() will resize the frame, with the dimantion (Tuple)
    return cv.resize(frame, dimenstion, interpolation=cv.INTER_AREA)


''' Reading Video And Resizing Them '''


def ReadVedio(path='Videos/6.mp4'):
    capture = cv.VideoCapture(path)

    while True:
        isTrue, frame = capture.read()
        # To resize the frame, pass it to the reScale(frame)
        resized_frame = reSclaeFrame(frame)

        # show the Actual frame.
        cv.imshow('Actual_Video', frame)
        # Show the resized frame.
        cv.imshow('ReSized_Video', resized_frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            print("Video ended")
            break
    capture.release()
    cv.destroyAllWindows()


'''ReSizing Images'''


def ReSizedImage(path='photos/7.jpg', wait=0, resized_scale=0.5):
    img = cv.imread('photos/7.jpg')  # Read the image.
    resized_img = reSclaeFrame(img, resized_scale)  # resized the image.
    cv.imshow("Actual_Image", img)  # show the actual image.
    cv.imshow('ReSized_Image', resized_img)  # show the resized image.
    cv.waitKey(wait)


def ReadLiveVedio():
    capture = cv.VideoCapture(0)

    while True:
        isTrue, frame = capture.read()

        cv.imshow("Live", frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()


""" This will set the Resulation for Live videos only. NOT FOR IMAGES """


def ChangeRes(width, height):
    """ The 3,4 is refrences for width and height"""
    capture.set(3, width)  # 3 refrences the width.
    capture.set(4, height)  # 4 refrences the height.


# ReSizedImage()
# ReadVedio('Videos/6.mp4')
ReadLiveVedio()
