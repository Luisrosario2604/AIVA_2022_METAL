#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_imper_detect.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Lllamando los algorithmos de detection + postprocecado
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import os
import shutil

from imperfection.main_imperfection import Imperfection


# return the class with most confidence sum
def get_class_most_confident_sum(classes_count, confidence_count):
    count_sum = [0., 0., 0.]
    for i, class_ in enumerate(classes_count):
        count_sum[class_] += confidence_count[i]
    return count_sum.index(max(count_sum))


class SystemRecognition:

    def __init__(self, image_path, algorithm):

        if not os.path.exists(image_path):
            raise Exception("\033[1m" + "[ERROR] -> File not existing" + "\033[0m")
        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            raise Exception("\033[1m" + "[ERROR] -> File is not an image" + "\033[0m")

        split = os.path.splitext(image_path)
        name = split[-2].split("/")[-1]

        self.image_path = image_path
        self.image_ext = split[-1][1:]
        self.image_name = name
        self.algorithm = algorithm
        self.list_class_imperfections = []

    def draw_all_classes_yoloV5(self):
        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')
        prog = "python3 ./yolov5/detect.py --weights ./yolov5/weights/best.pt --img 416 --conf 0.4 --source" + str(self.image_path)
        os.system(prog)

        if not os.path.isdir('./results'):
            os.mkdir('./results')
        shutil.copyfile("./yolov5/runs/detect/exp/" + self.image_name + "." + self.image_ext, "./results/" + self.image_name + "." + self.image_ext)
        print("\033[1m" + "[INFO] -> Results are in \"results\" directory" + "\033[0m")

    def detect_yoloV5(self):
        classes_count = []
        confidence_count = []
        self.list_class_imperfections = []

        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')
        prog = "python3 ./yolov5/detect.py --weights ./yolov5/weights/best.pt --img 416 --conf 0.4 --save-conf --source " + str(self.image_path) + " --nosave " + "--save-txt"
        os.system(prog)
        print("\n___________________________________________________________\n\n")
        with open("./yolov5/runs/detect/exp/labels/" + self.image_name + ".txt") as f:
            lines = f.readlines()
            for line in lines:
                classes_count.append(int(line.split(' ')[0]))
                confidence_count.append(float(line.split(' ')[5]))
            class_most_conf = get_class_most_confident_sum(classes_count, confidence_count)
            for line in lines:
                l = line.split(' ')
                if int(l[0]) == class_most_conf:
                    self.list_class_imperfections.append(Imperfection(float(l[1]), float(l[2]), float(l[3]), float(l[4]), int(l[0])))

        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')

    def print_info(self):
        print("\033[1m" + "[CLASS] System Recognition" "\033[0m")
        print("\t\timage path =\t\t", self.image_path)
        print("\t\timage name =\t\t", self.image_name)
        print("\t\timage extension =\t", self.image_ext)
        print("\t\talgorithm used =\t", self.algorithm)
        if self.list_class_imperfections:
            for i, imperfection in enumerate(self.list_class_imperfections):
                imperfection.print_info(i)
