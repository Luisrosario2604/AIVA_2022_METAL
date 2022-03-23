#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL yolo_implementation.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Detección de defectos en imágenes de superficies de metal con yolo
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import random


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

    xmin = random.randint(0, width)
    ymin = random.randint(0, height)
    xmax = random.randint(xmin, width)
    ymax = random.randint(ymin, height)
    location = [xmin, ymin, xmax, ymax]

    label = random.randint(0, 2)

    return label, location
