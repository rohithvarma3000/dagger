HEADER = "$M"
DIRECTION_IN = "<"
DIRECTION_OUT = ">"


def get_header_bytes():
    return bytearray(HEADER)


def get_direction_in_bytes():
    return bytearray(DIRECTION_IN)


def get_direction_out_bytes():
    return bytearray(DIRECTION_OUT)


def calculate_crc(byte_array):
    crc = 0
    for byte in byte_array:
        crc ^= byte
    return crc


def test_import():
    pass
