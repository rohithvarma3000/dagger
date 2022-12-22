HEADER = "$M"
DIRECTION_IN = "<"
DIRECTION_OUT = ">"


def get_header_bytes():
    return bytearray(HEADER, "utf-8")


def get_direction_in_bytes():
    return bytearray(DIRECTION_IN, "utf-8")


def get_direction_out_bytes():
    return bytearray(DIRECTION_OUT, "utf-8")


def calculate_crc(byte_array):
    crc = 0
    for byte in byte_array:
        crc ^= byte
    return crc
