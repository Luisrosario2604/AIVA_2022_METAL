#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_algorithm.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Detección de defectos en imágenes de superficies de metal
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import numpy as np
import cv2
from imper_detect.main_imper_detect import ImperDetect

# Global variables

# Class declarations


# Function declarations
def check_connection(a):
    return a + 1


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="path of the data file")
    ap.add_argument("-s", "--store_result", required=False, help="store the result", action='store_true')
    return vars(ap.parse_args())


def main():
    args = get_arguments()
    image_path = args["file"]

    imper = ImperDetect(image_path, "yoloV5")
    imper.detection()
    imper.print_info()

    if args["store_result"]:
        imper.draw_all_classes_yoloV5()


# Main body
if __name__ == '__main__':
    main()
