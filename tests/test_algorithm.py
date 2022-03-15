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
from algorithm.main_algorithm import check_connection


# Function declarations

# Fork
@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 2),
    (3, 4),
    (4, 5),
    (5, 6),
])
def test_multi_algorithm(test_input, expected):
    assert check_connection(test_input) is expected


@pytest.mark.xfail
def test_fail_algorithm():
    assert check_connection(1) == 0


# @pytest.mark.skip(reason="classification not supported yet")
# def test_classification():
#     someImages = "Img/test"
#     assert classification_result(someImages) == 0
