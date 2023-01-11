HEADER = "$M"
DIRECTION_IN = "<"
DIRECTION_OUT = ">"
ZERO = 0


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


def send_out(con, code):
    header = get_header_bytes()
    direction = get_direction_in_bytes()

    length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
    code_bytes = bytearray(code.to_bytes(1, byteorder="little"))
    message = length_bytes + code_bytes
    crc = calculate_crc(message)
    packet = header + direction + message
    packet.append(crc)
    con.send(packet)
