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
        self.__x = x
        self.__y = y
        self.__h = h
        self.__w = w
        self.__classification = classification
        self.__confidence = confidence

    def get_coords_class(self):
        return [self.__classification, self.__x, self.__y, self.__h, self.__w, self.__confidence]

    def print_info(self, number=0):
        print("\033[1m" + "[CLASS] Imperfection " + str(number) + "\033[0m", end="")
        print("\tx:" + str(self.__x) +
              "  y:" + str(self.__y) +
              "  w:" + str(self.__w) +
              "  h:" + str(self.__h) +
              "  class:" + str(self.__classification) +
              "  confidence:" + str(self.__confidence))
