import cv2 as cv
from cv2 import resize
import numpy as np
from cv2 import VideoCapture


def rescal(frame, scale=1.5):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w,h)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


capture = VideoCapture(0)
if not capture.isOpened():
    print('Open Vedio')
    exit()
    
# methode 2 rezise image and video 
def rechage_1280x720():
    capture.set(3, 1280)
    capture.set(4, 720)

def rechange_generater(w,h):
    capture.set(3, w)
    capture.set(4, h)

# rechage_1280x720() auto set
# rechange_generater(2000, 168) set by uder input scale

while True:
    ret, frame = capture.read()
    if not ret:
        print('Can not recive frame ')
        exit()
        break

    # resizeV = rescal(frame) call by rescal 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('User', gray)
    if cv.waitKey(1) == ord('q'):
        break
capture.relese()
cv.destroyAllWindows()