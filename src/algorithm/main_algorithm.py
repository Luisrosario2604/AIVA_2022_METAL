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
from yolo_v5.main_yolo_v5 import YOLOv5
# from fast_rcnn.main_fast_rcnn import FastRcnn


# Function declarations
def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="path of the data file")
    ap.add_argument("-s", "--store_result", required=False, help="store the result", action='store_true')
    return vars(ap.parse_args())


def main():
    args = get_arguments()
    image_path = args["file"]

    yolov5 = YOLOv5(image_path)
    yolov5.detect()
    yolov5.print_info()

    print("\n")
    print("Algorithm : " + str(yolov5.get_algorithm()))
    print("Imperfections : " + str(yolov5.get_imperfections()))
    print("Class : " + str(yolov5.get_class_most_conf()))
    print("Image : " + str(yolov5.get_image()))

    if args["store_result"]:
        yolov5.draw()


# Main body
if __name__ == '__main__':
    main()
