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


class ImperDetect:

    def __init__(self, image_path):

        if not os.path.exists(image_path):
            raise Exception("\033[1m" + "[ERROR] -> File not existing" + "\033[0m")
        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            raise Exception("\033[1m" + "[ERROR] -> File is not an image" + "\033[0m")

        split = os.path.splitext(image_path)

        name = split[-2].split("/")[-1]

        self.image_path = image_path
        self.image_ext = split[-1][1:]
        self.image_name = name

    def draw(self):
        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')
        prog = "python3 ./yolov5/detect.py --weights ./yolov5/weights/best.pt --img 416 --conf 0.4 --source " + str(self.image_path)
        os.system(prog)

        if not os.path.isdir('./results'):
            os.mkdir('./results')
        shutil.copyfile("./yolov5/runs/detect/exp/" + self.image_name + "." + self.image_ext, "./results/" + self.image_name + "." + self.image_ext)
        print("\033[1m" + "[INFO] -> Results are in \"results\" directory" + "\033[0m")

    def detection(self):
        detections = []
        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')
        prog = "python3 ./yolov5/detect.py --weights ./yolov5/weights/best.pt --img 416 --conf 0.4 --source " + str(self.image_path) + " --nosave " + " --save-txt"
        os.system(prog)
        with open("./yolov5/runs/detect/exp/labels/" + self.image_name + ".txt") as f:
            lines = f.readlines()
            for line in lines:
                l = line.split(' ')
                detections.append(Imperfection(l[1], l[2], l[3], l[4], l[0]))

        return detections

    def print_info(self):
        print("Imperfection :")
        print("\t\tpath = ", self.image_path)
        print("\t\tname = ", self.image_name)
        print("\t\text = ", self.image_ext)

