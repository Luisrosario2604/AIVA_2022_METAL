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

# Global variables

# Class declarations


# Function declarations
def check_connection(a):
    return a + 1


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="path of the data file")
    return vars(ap.parse_args())


def main():
    args = get_arguments()

    a = np.matrix([[1, 2], [3, 4]])
    print(a.dtype)
    print(a)

    print(args['file'])


# Main body
if __name__ == '__main__':
    main()
