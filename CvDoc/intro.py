import cv2 as cv
from cv2 import VideoCapture
from cv2 import resize
import numpy as np

# methode 1 rezise image and video 
def rescal(frame, scale=1.50):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w,h)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


img = cv.imread("/home/pised/Documents/Opencv/CvDoc/Resources/Photos/cat.jpg")
img2 = cv.imread("/home/pised/Documents/Opencv/CvDoc/Resources/Photos/park.jpg")
img3 = cv.imread("/home/pised/Documents/Opencv/CvDoc/Resources/Photos/cats.jpg")

reImage = rescal(img)
cvtImg  = cv.cvtColor(reImage, cv.COLOR_BGR2GRAY)
cv.imshow('cat', cvtImg)

reImage2 = rescal(img2)
cvtImg2  = cv.cvtColor(reImage2, cv.COLOR_BGR2GRAY)
cv.imshow('cat', cvtImg2)

reImage3 = rescal(img3)
cvtImg3  = cv.cvtColor(reImage3, cv.COLOR_BGR2GRAY)
cv.imshow('cat', cvtImg3)

cv.waitKey(0)
cv.destroyAllWindows()

