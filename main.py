#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Detección de defectos en imágenes de superficies de metal
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse

# Global variables

# Class declarations

# Function declarations


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="path of the data file")
    return vars(ap.parse_args())


def main():
    args = get_arguments()

    print(args['file'])


# Main body
if __name__ == '__main__':
    main()
