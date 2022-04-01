#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_imper_detect.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Detección de defectos en imágenes de superficies de metal con yolo
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import os
import shutil

from imperfection.main_imperfection import Imperfection
from system_recognition.main_system_recognition import SystemRecognition


class ImperDetect:

    def __init__(self, image_path, algorithm="yoloV5"):
        self.image_path = image_path
        self.algorithm = algorithm
        self.class_system_recognition = SystemRecognition(image_path, algorithm)

    def draw(self):
        print("draw")

    def detection(self):
        if self.algorithm == "yoloV5":
            self.class_system_recognition.detect_yoloV5()

    def print_info(self):
        print("\033[1m" + "[CLASS] Imper Detect" "\033[0m")
        print("\t\timage path =\t\t", self.image_path)
        print("\t\talgorithm used =\t", self.algorithm)
        self.class_system_recognition.print_info()
