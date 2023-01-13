import dagger.utils as util
import random


def test_get_header_bytes():
    header = util.get_header_bytes()
    assert chr(header[0]) == "$"
    assert chr(header[1]) == "M"


def test_get_direction_in_bytes():
    direction = util.get_direction_in_bytes()
    assert chr(direction[0]) == "<"


def test_get_direction_out_bytes():
    direction = util.get_direction_out_bytes()
    assert chr(direction[0]) == ">"


def test_calculate_crc():
    test_nums = []
    check_crc = 0
    for _ in range(10):
        rand_integer = random.randint(0, 256)
        check_crc ^= rand_integer
        test_nums.append(rand_integer)
    bytes_nums = bytearray(test_nums)
    func_crc = util.calculate_crc(bytes_nums)
    assert func_crc == check_crc
