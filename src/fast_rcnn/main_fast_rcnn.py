#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_fast_rcnn.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Lllamando los algorithmos de detection + postprocecado para fast_rcnn
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import os

from system_recognition.main_system_recognition import SystemRecognition


class FastRcnn(SystemRecognition):

    def __init__(self, image_path):

        if not os.path.exists(image_path):
            raise Exception("\033[1m" + "[ERROR] -> File not existing" + "\033[0m")
        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            raise Exception("\033[1m" + "[ERROR] -> File is not an image" + "\033[0m")

        split = os.path.splitext(image_path)
        name = split[-2].split("/")[-1]

        self.__image_path = image_path
        self.__image_ext = split[-1][1:]
        self.__image_name = name
        self.__list_class_imperfections = []
        self.__class_most_conf = None

    def detect(self):
        print("This function is in development ...")
        return None

    def draw(self):
        print("This function is in development ...")
        return None

    def get_class_most_conf(self):
        return self.__class_most_conf

    def get_image(self):
        return [self.__image_path, self.__image_name, self.__image_ext]

    def get_imperfections(self):
        class_imperfections = self.__list_class_imperfections
        return [i.get_coords_class() for i in class_imperfections]

    def get_algorithm(self):
        return "Fast-RCNN"

    def print_info(self):
        print("\033[1m" + "[CLASS] System Recognition" "\033[0m")
        print("\t\timage path =\t\t", self.__image_path)
        print("\t\timage name =\t\t", self.__image_name)
        print("\t\timage extension =\t", self.__image_ext)
        if self.__list_class_imperfections:
            for i, imperfection in enumerate(self.__list_class_imperfections):
                imperfection.print_info(i)
