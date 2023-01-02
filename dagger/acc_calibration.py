from dagger.utils import get_header_bytes, get_direction_in_bytes, calculate_crc


class AccCalibration:
    __msg_length = 0
    __msg_code = 205

    def __init__(self, connection):
        self._connection = connection
        self.cmd = 0

    def acc_calibartion(self):
        header = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(
            AccCalibration.__msg_length.to_bytes(1, byteorder="little")
        )
        code_bytes = bytearray(
            AccCalibration.__msg_code.to_bytes(1, byteorder="little")
        )

        message = length_bytes + code_bytes
        crc = calculate_crc(message)
        packet = header + direction + message
        packet.append(crc)
        self._connection.send(packet)
