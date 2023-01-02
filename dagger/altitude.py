import struct
from dagger.utils import get_direction_in_bytes, get_header_bytes, calculate_crc, ZERO


class AltitudeData:
    def __init__(self, altitude, vario):
        self.altitude = altitude
        self.vario = vario


class Altitude:
    __msg_code = 109
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection

    def get_(self):  # function for requesting the out packet
        header = get_header_bytes()
        direction = (
            get_direction_in_bytes()
        )  # Requesting the out packet using an in direction as mentioned in docs
        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(Altitude.__msg_code.to_bytes(1, byteorder="little"))
        message = length_bytes + code_bytes  # no payload data
        crc = calculate_crc(message)
        packet = header + direction + message
        packet.append(crc)
        self._connection.send(packet)

        try:
            header_out = struct.unpack("cc", self._connection.recv(2))[0]
            direction_out = struct.unpack("c", self._connection.recv(1))[0]
            length_out = struct.unpack("B", self._connection.recv(1))[0]
            code_out = struct.unpack("B", self._connection.recv(1))[0]
            altitude = struct.unpack("<i", self._connection.recv(4))[
                0
            ]  # signed int of 4 bytes hence i
            vario = struct.unpack("<h", self._connection.recv(2))[
                0
            ]  # signed int of 2 bytes hence h
            crc_out = struct.unpack("B", self._connection.recv(1))[0]

            obj = AltitudeData(altitude, vario)
            return obj

        except:
            print("Data not recieved/some error occured")
