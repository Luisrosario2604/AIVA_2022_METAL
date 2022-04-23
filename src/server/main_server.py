#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** AIVA_2022_METAL server.py
# ** Natalia / Vicent / Luis, 2022
# ** File description:
# ** Server for application
# ** https://github.com/natalialperez
# ** https://github.com/vgilabert94
# ** https://github.com/Luisrosario2604
# */

# Imports
from flask import Flask
from flask import jsonify
from flask import request
import cv2
import numpy as np
import base64
from os.path import exists

from yolo_v5.main_yolo_v5 import YOLOv5
from fast_rcnn.main_fast_rcnn import FastRcnn


# Function declaration
def create_app():
    return Flask(__name__)


app = create_app()


def base64_to_path(base64_image):
    image_path = "./dataset/tmp_img.png"
    encoded_data = base64_image.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(image_path, img)

    return image_path


def imperfections_to_dictionary(imperfections):
    return [{
            "Class": i[0],
            "x": i[1],
            "y": i[2],
            "width": i[3],
            "height": i[4],
            "confidence": i[5]} for i in imperfections]


def append_image():
    path = "results/result.png"
    base64_result = "File not found !"
    if exists(path):
        with open(path, "rb") as img_file:
            base64_result = base64.b64encode(img_file.read())
        base64_result = base64_result.decode('utf-8')

    return base64_result


def make_json(algorithm, class_most_conf, imperfections, add_result_image=False):
    dic = imperfections_to_dictionary(imperfections)
    if add_result_image:
        data = {
            'Algorithm': algorithm,
            'Class': class_most_conf,
            'Imperfections': dic,
            'Result image': append_image()
        }
    else:
        data = {
            'Algorithm': algorithm,
            'Class': class_most_conf,
            'Imperfections': dic
        }
    return jsonify(data)


@app.route('/detect/yolov5', methods=['POST'])
def post_detect_yolo_v5():
    json_data = request.json
    try:
        base64_string = json_data["base64_image"]
    except Exception:
        return jsonify({'Error': 'base64_image parameter not found !'}), 404

    image_path = base64_to_path(base64_string)
    yolov5 = YOLOv5(image_path)
    yolov5.detect()

    return make_json(
        yolov5.get_algorithm(),
        yolov5.get_class_most_conf(),
        yolov5.get_imperfections()
    ), 200


@app.route('/detect_and_draw/yolov5', methods=['POST'])
def post_detect_and_draw_yolo_v5():
    json_data = request.json
    try:
        base64_string = json_data["base64_image"]
    except Exception:
        return jsonify({'Error': 'base64_image parameter not found !'}), 404

    image_path = base64_to_path(base64_string)

    yolov5 = YOLOv5(image_path)
    yolov5.detect()
    yolov5.draw()

    return make_json(
        yolov5.get_algorithm(),
        yolov5.get_class_most_conf(),
        yolov5.get_imperfections(),
        True
    ), 200


@app.route('/detect/fast_rcnn', methods=['POST'])
def post_detect_fast_rcnn():
    json_data = request.json
    try:
        base64_string = json_data["base64_image"]
    except Exception:
        return jsonify({'Error': 'base64_image parameter not found !'}), 404

    image_path = base64_to_path(base64_string)

    fast_rcnn = FastRcnn(image_path)
    fast_rcnn.detect()

    return make_json(
        fast_rcnn.get_algorithm(),
        fast_rcnn.get_class_most_conf(),
        fast_rcnn.get_imperfections(),
    ), 200


@app.route('/detect_and_draw/fast_rcnn', methods=['POST'])
def post_detect_and_draw_fast_rcnn():
    json_data = request.json
    try:
        base64_string = json_data["base64_image"]
    except Exception:
        return jsonify({'Error': 'base64_image parameter not found !'}), 404

    image_path = base64_to_path(base64_string)

    fast_rcnn = FastRcnn(image_path)
    fast_rcnn.detect()
    fast_rcnn.draw()

    return make_json(
        fast_rcnn.get_algorithm(),
        fast_rcnn.get_class_most_conf(),
        fast_rcnn.get_imperfections(),
        False
    ), 200


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'Error': str(error)}), 404


# Main body
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8100)
