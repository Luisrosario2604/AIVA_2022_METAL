#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_imperfection.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Clase para obtener las coordenada y classe
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

class Imperfection:
    def __init__(self, x, y, h, w, classification, confidence):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.classification = classification
        self.confidence = confidence

    def get_coords_class(self):
        return [self.classification, self.x, self.y, self.h, self.w, self.confidence]

    def print_info(self, number=0):
        print("\033[1m" + "[CLASS] Imperfection " + str(number) + "\033[0m", end="")
        print("\tx:" + str(self.x) +
              "  y:" + str(self.y) +
              "  w:" + str(self.w) +
              "  h:" + str(self.h) +
              "  class:" + str(self.classification) +
              "  confidence:" + str(self.confidence))
