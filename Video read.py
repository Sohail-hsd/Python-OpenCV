import cv2 as cv

'''Reading Video'''
# you can pass path of a video, OR you can pass a number 0,1 for capture frames form webcame.
capture = cv.VideoCapture('Videos/6.mp4')

# to read videos frame by frame.
while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    # to stope the video.
    if cv.waitKey(20) & 0xFF == ord('d'):
        print("Frams ended.")
        break

capture.release()
cv.destroyAllWindows()
