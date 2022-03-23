from cv2 import cv2
import random
import os


# Defect classifier and locator of imperfections in images.
def classify_and_locate(img):
    '''
    TYPE OF DEFECTS:
    0: inclusions
    1: scratches
    2: patches
    -------------------------------------------
    location = [xmin, ymin, xmax, ymax] in pixels
    size = [width, height, depth] in pixels
    '''
    height, width, channels = img.shape

    xmin = random.randint(0,width)
    ymin = random.randint(0,height)
    xmax = random.randint(xmin,width)
    ymax = random.randint(ymin,height)
    location = [xmin,ymin,xmax,ymax]
    
    label = random.randint(0,2)
    
    return label, location
    