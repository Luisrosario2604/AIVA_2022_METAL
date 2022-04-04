#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Tests Algorithm
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

# Imports
import pytest
import os
import sys
import filecmp

from imper_detect.main_imper_detect import ImperDetect

imper_no_detect = ImperDetect("dataset/IMAGES/inclusion_1.jpg", "yoloV5")
imper1 = ImperDetect("dataset/IMAGES/inclusion_1.jpg", "yoloV5")
imper_rcnn = ImperDetect("dataset/IMAGES/inclusion_1.jpg", "Fast_RCNN")
imper1.detection()


# Function declarations
def test_imper_detect_creation_functions_0():
    assert imper1.get_class_system_recognition().get_algorithm() == "yoloV5"


def test_imper_detect_creation_functions_1():
    # we cant test this because confidence are never the same
    #
    # assert imper1.get_class_system_recognition().get_imperfections() == [[0, 0.6225, 0.235, 0.085, 0.16, 0.404081],
    #                                                                     [0, 0.1975, 0.0975, 0.075, 0.155, 0.472998],
    #                                                                     [0, 0.615, 0.785, 0.13, 0.43, 0.62408],
    #                                                                     [0, 0.635, 0.4575, 0.13, 0.215, 0.655571]]
    imper1.get_class_system_recognition().get_imperfections()
    assert str(imper1.get_class_system_recognition().get_class_most_conf()) == "0"


def test_imper_detect_creation_functions_2():
    assert str(imper1.get_class_system_recognition().get_class_most_conf()) == "0"


def test_imper_detect_creation_functions_3():
    assert imper1.get_class_system_recognition().get_image() == ['dataset/IMAGES/inclusion_1.jpg', 'inclusion_1', 'jpg']


def test_imper_detect_draw():
    imper1.draw()
    exist = os.path.isfile("./results/inclusion_1.jpg")
    assert exist


def test_imper_print_info():
    orig_stdout = sys.stdout
    with open('./tests/out1.txt', 'w') as f:
        sys.stdout = f
        imper1.print_info()
        sys.stdout = orig_stdout
    assert str(imper1.get_class_system_recognition().get_class_most_conf()) == "0"


def test_imper_with_rcnn():
    orig_stdout = sys.stdout
    with open('./tests/out1_1.txt', 'w') as f:
        sys.stdout = f

        imper_rcnn.detection()
        imper_rcnn.print_info()
        print("Algorithm : " + str(imper_rcnn.get_class_system_recognition().get_algorithm()))
        print("Imperfections : " + str(imper_rcnn.get_class_system_recognition().get_imperfections()))
        print("Class : " + str(imper_rcnn.get_class_system_recognition().get_class_most_conf()))
        print("Image : " + str(imper_rcnn.get_class_system_recognition().get_image()))
        imper_rcnn.draw()

        sys.stdout = orig_stdout

    assert filecmp.cmp('./tests/out1_0.txt', './tests/out1_1.txt')


@pytest.mark.xfail
def test_fail_algorithm_no_use_of_detection_0():
    assert imper_no_detect.get_class_system_recognition().get_algorithm() == "yoloV5"


@pytest.mark.xfail
def test_fail_algorithm_no_use_of_detection_1():
    assert imper_no_detect.get_class_system_recognition().get_imperfections() == [[0, 0.6225, 0.235, 0.085, 0.16, 0.404081],
                                                                                  [0, 0.1975, 0.0975, 0.075, 0.155, 0.472998],
                                                                                  [0, 0.615, 0.785, 0.13, 0.43, 0.62408],
                                                                                  [0, 0.635, 0.4575, 0.13, 0.215, 0.655571]]


@pytest.mark.xfail
def test_fail_algorithm_no_use_of_detection_2():
    assert imper_no_detect.get_class_system_recognition().get_class_most_conf() == 0


@pytest.mark.xfail
def test_fail_algorithm_no_use_of_detection_3():
    assert imper_no_detect.get_class_system_recognition().get_image() == ['dataset/IMAGES/inclusion_1.jpg', 'inclusion_1', 'jpg']


def test_fail_algorithm_bad_image_0():
    with pytest.raises(Exception):
        ImperDetect("Fast_RCNN")


def test_fail_algorithm_bad_image_1():
    with pytest.raises(Exception):
        ImperDetect("dataset/IMAGES/inclusion_1.pdf")
