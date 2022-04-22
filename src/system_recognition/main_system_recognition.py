#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_imper_detect.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** interfaz
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

from abc import ABC, abstractmethod


class SystemRecognition(ABC):

    @abstractmethod
    def detect(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_class_most_conf(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def get_imperfections(self):
        pass

    @abstractmethod
    def get_algorithm(self):
        pass

    @abstractmethod
    def print_info(self):
        pass
