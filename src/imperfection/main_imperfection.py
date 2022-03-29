#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_imperfection.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Detección de defectos en imágenes de superficies de metal con yolo
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

class Imperfection:
    def __init__(self, x, y, h, w, classification):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.classification = classification

    def print_info(self):
        print("Imperfection :")
        print("\t\tx = ", self.x)
        print("\t\ty = ", self.y)
        print("\t\th = ", self.h)
        print("\t\tw = ", self.w)
        print("\t\tClass = ", self.classification)
