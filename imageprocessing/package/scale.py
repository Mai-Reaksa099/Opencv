import cv2 as cv
import numpy as np
from cv2 import VideoCapture 
capture = VideoCapture(0)

def rescal(frame, scale=1.5):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w,h)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def rechage_1280x720():
    capture.set(3, 1280)
    capture.set(4, 720)

def rechange_generater(w,h):
    capture.set(3, w)
    capture.set(4, h)
