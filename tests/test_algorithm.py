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
import os

from yolo_v5.main_yolo_v5 import YOLOv5
from fast_rcnn.main_fast_rcnn import FastRcnn
from imperfection.main_imperfection import Imperfection

image_path = "dataset/IMAGES/inclusion_1.jpg"
yolov5 = YOLOv5(image_path)
fast_rcnn = FastRcnn(image_path)
yolov5.detect()


# Function declarations
def test_impefection():
    imper = Imperfection(1, 2, 3, 4, 0, 0.2)
    assert imper.get_coords_class() == [0, 1, 2, 3, 4, 0.2]


def test_yolo_v5_get_algorithm():
    assert str(yolov5.get_algorithm()) == "Yolo V5"


def test_yolo_v5_get_class_most_conf():
    assert yolov5.get_class_most_conf() == 0


def test_yolo_v5_get_image_1():
    assert str(yolov5.get_image()[0]) == "dataset/IMAGES/inclusion_1.jpg"


def test_yolo_v5_get_image_2():
    assert str(yolov5.get_image()[1]) == "inclusion_1"


def test_yolo_v5_get_image_3():
    assert str(yolov5.get_image()[2]) == "jpg"


def test_yolo_v5_get_imperfections():
    imperfection = yolov5.get_imperfections()
    yolov5.print_info()

    result = 1

    if len(imperfection) != 4:
        result = 0
    if imperfection[0][0] != 0:
        result = 0
    if imperfection[1][0] != 0:
        result = 0
    if imperfection[2][0] != 0:
        result = 0
    if imperfection[3][0] != 0:
        result = 0

    assert result == 1


def test_yolo_v5_draw():
    yolov5.draw()
    assert os.path.isfile("./results/result.jpg")


def test_fast_rcnn_get_algorithm():
    assert str(fast_rcnn.get_algorithm()) == "Fast-RCNN"


def test_fast_rcnn_detect():
    if fast_rcnn.detect() is None:
        assert True
    else:
        assert False


def test_fast_rcnn_draw():
    fast_rcnn.print_info()
    if fast_rcnn.draw() is None:
        assert True
    else:
        assert False


def test_fast_rcnn_get_class_most_conf():
    if fast_rcnn.get_class_most_conf() is None:
        assert True
    else:
        assert False


def test_fast_rcnn_get_image_1():
    assert str(fast_rcnn.get_image()[0]) == "dataset/IMAGES/inclusion_1.jpg"


def test_fast_rcnn_get_image_2():
    assert str(fast_rcnn.get_image()[1]) == "inclusion_1"


def test_fast_rcnn_get_image_3():
    assert str(fast_rcnn.get_image()[2]) == "jpg"


def test_fast_rcnn_get_imperfections():
    assert len(fast_rcnn.get_imperfections()) == 0


def test_yolo_v5_error_bad_ext():
    try:
        image_path = "image.blabla"
        YOLOv5(image_path)
        assert False
    except Exception:
        assert True


def test_yolo_v5_error_not_existing():
    try:
        image_path = "image.jpg"
        YOLOv5(image_path)
        assert False
    except Exception:
        assert True


def test_fast_rcnn_error_bad_ext():
    try:
        image_path = "image.blabla"
        FastRcnn(image_path)
        assert False
    except Exception:
        assert True


def test_fast_rcnn_error_not_existing():
    try:
        image_path = "image.jpg"
        FastRcnn(image_path)
        assert False
    except Exception:
        assert True
