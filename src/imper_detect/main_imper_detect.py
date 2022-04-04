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


from system_recognition.main_system_recognition import SystemRecognition


class ImperDetect:

    def __init__(self, image_path, algorithm="yoloV5"):
        if algorithm not in ["yoloV5", "Fast_RCNN"]:
            raise Exception("\033[1m" + "[ERROR] -> Algorithm as not a vadid name" + "\033[0m")

        self.class_system_recognition = SystemRecognition(image_path, algorithm)
        self.detection_called = False

    def detection(self):
        if self.class_system_recognition.get_algorithm() == "yoloV5":
            self.class_system_recognition.detect_yoloV5()
        elif self.class_system_recognition.get_algorithm() == "Fast_RCNN":
            self.class_system_recognition.draw_fastRCNN()

        self.detection_called = True

    def draw(self):
        if not self.detection_called:
            raise Exception("\033[1m" + "[ERROR] -> You should call \"detection\" method before using this one" + "\033[0m")
        if self.class_system_recognition.get_algorithm() == "yoloV5":
            self.class_system_recognition.draw_yoloV5()
        elif self.class_system_recognition.get_algorithm() == "Fast_RCNN":
            self.class_system_recognition.draw_fastRCNN()

    def get_class_system_recognition(self):
        if not self.detection_called:
            raise Exception("\033[1m" + "[ERROR] -> You should call \"detection\" method before using this one" + "\033[0m")
        return self.class_system_recognition

    def print_info(self):
        print("\033[1m" + "[CLASS] Imper Detect" "\033[0m")
        self.class_system_recognition.print_info()
