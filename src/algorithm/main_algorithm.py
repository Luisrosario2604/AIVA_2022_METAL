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
# import cv2
# from file_manager import open_image

# Global variables

# Class declarations


# Function declarations
def check_connection(a):
    return a + 1


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="path of the data file")
    ap.add_argument("-s", "--show_example", required=False, help="shows an example image", action='store_true')
    return vars(ap.parse_args())


def main():
    args = get_arguments()

    # image = open_image(args["file"])

    # if args["show_example"]:
    #     cv2.imshow('image', image)
    #     cv2.waitKey()

    a = np.matrix([[1, 2], [3, 4]])
    print(a.dtype)
    print(a)

    print(args['file'])


# Main body
if __name__ == '__main__':
    main()
