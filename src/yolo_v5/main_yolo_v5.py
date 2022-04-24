#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL main_yolo_v5.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Lllamando los algorithmos de detection + postprocecado para yolov5
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

import os
import shutil
import cv2

from imperfection.main_imperfection import Imperfection
from system_recognition.main_system_recognition import SystemRecognition


# return the class with most confidence sum
def get_class_most_confident_sum(classes_count, confidence_count):
    count_sum = [0., 0., 0.]
    for i, class_ in enumerate(classes_count):
        count_sum[class_] += confidence_count[i]
    return count_sum.index(max(count_sum))


class YOLOv5(SystemRecognition):

    def __init__(self, image_path):

        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            raise Exception("\033[1m" + "[ERROR] -> File is not an image" + "\033[0m")
        if not os.path.exists(image_path):
            raise Exception("\033[1m" + "[ERROR] -> File not existing" + "\033[0m")

        split = os.path.splitext(image_path)
        name = split[-2].split("/")[-1]

        self.__image_path = image_path
        self.__image_ext = split[-1][1:]
        self.__image_name = name
        self.__list_class_imperfections = []
        self.__class_most_conf = None

    def detect(self):
        classes_count = []
        confidence_count = []
        self.__list_class_imperfections = []

        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')
        prog = "python3 ./yolov5/detect.py --weights ./yolov5/weights/best.pt --img 416 --conf 0.4 --save-conf --source "\
               + str(self.__image_path) + " --nosave " + "--save-txt"
        os.system(prog)
        print("\n___________________________________________________________\n\n")
        if not os.path.isfile(("./yolov5/runs/detect/exp/labels/" + self.__image_name + ".txt")):
            self.__list_class_imperfections.append(Imperfection(0, 0, 0, 0, 0, 0))
        else:
            with open("./yolov5/runs/detect/exp/labels/" + self.__image_name + ".txt") as f:
                lines = f.readlines()
                for line in lines:
                    classes_count.append(int(line.split(' ')[0]))
                    confidence_count.append(float(line.split(' ')[5]))
                self.__class_most_conf = get_class_most_confident_sum(classes_count, confidence_count)
                for line in lines:
                    splited = line.split(' ')
                    if int(splited[0]) == self.__class_most_conf:
                        self.__list_class_imperfections.append(Imperfection(float(splited[1]),
                                                                            float(splited[2]),
                                                                            float(splited[3]),
                                                                            float(splited[4]),
                                                                            int(splited[0]),
                                                                            float(splited[5])))

        if os.path.isdir('./yolov5/runs'):
            shutil.rmtree('./yolov5/runs')

    def draw(self):
        img = cv2.imread(self.__image_path)
        dim = img.shape
        result_list = []
        imperfections = self.get_imperfections()
        label_str = ""
        classification = 0
        drawed = None

        for imper in imperfections:
            classification = imper[0]
            x = imper[1]
            y = imper[2]
            w = imper[3]
            h = imper[4]
            confidence = imper[5]

            print("0 -> " + str(imper))

            x1 = max(int((x - w / 2) * dim[1]), 0)
            y1 = min(int((y - h / 2) * dim[0]), dim[0])
            x2 = max(int((x + w / 2) * dim[1]), 0)
            y2 = min(int((y + h / 2) * dim[0]), dim[0])
            result_list.append(confidence)

            drawed = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

        if classification == 0:
            label_str = "inclusion"
        elif classification == 1:
            label_str = "patches"
        elif classification == 2:
            label_str = "scratches"
        result_mean = sum(result_list) / len(result_list)
        text_to_draw = label_str + ":  " + str(result_mean)
        drawed = cv2.putText(img=drawed, text=text_to_draw, org=(20, 20), fontFace=0, fontScale=0.5, color=(0, 0, 255), thickness=1)

        if not os.path.isdir('./results'):
            os.mkdir('./results')
        cv2.imwrite("./results/" + "result." + self.__image_ext, drawed)
        print("\033[1m" + "[INFO] -> Image result in \"results\" directory" + "\033[0m")

    def get_class_most_conf(self):
        return self.__class_most_conf

    def get_image(self):
        return [self.__image_path, self.__image_name, self.__image_ext]

    def get_imperfections(self):
        class_imperfections = self.__list_class_imperfections
        return [i.get_coords_class() for i in class_imperfections]

    def get_algorithm(self):
        return "Yolo V5"

    def print_info(self):
        print("\033[1m" + "[CLASS] System Recognition" "\033[0m")
        print("\t\timage path =\t\t", self.__image_path)
        print("\t\timage name =\t\t", self.__image_name)
        print("\t\timage extension =\t", self.__image_ext)
        if self.__list_class_imperfections:
            for i, imperfection in enumerate(self.__list_class_imperfections):
                imperfection.print_info(i)
