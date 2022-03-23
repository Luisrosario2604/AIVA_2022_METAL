#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL file_manager.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** File manager
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import cv2
from yolo_implementation import classify_and_locate


# Loads one image
def open_image(path):
    inputPath = path
    # print('Image loaded ...')
    img = cv2.imread(inputPath)
    label, location = classify_and_locate(img)

    if label == 0:
        text_label = 'inclusions'
    elif label == 1:
        text_label = 'scratches'
    elif label == 2:
        text_label = 'patches'

    # print('Etiqueta del defecto: ' + str(label) + " = " + text_label)
    # print('Location: ' + str(location))

    test_img = cv2.rectangle(img, (location[0], location[1]), (location[2], location[3]), (255, 0, 0), 2)
    test_img = cv2.putText(test_img, text_label, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)

    return test_img