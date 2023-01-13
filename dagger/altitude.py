import struct
import time
from dagger.utils import get_direction_in_bytes, get_header_bytes, calculate_crc, ZERO


class AltitudeData:
    def __init__(self, altitude, vatio):
        self.altitude = altitude
        self.vatio = vatio
        self.timestamp = time.time()


class Altitude:

    __msg_code = 109
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection

    def get_altitude_data(self):
        """Requests the OUT package."""
        header = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(Altitude.__msg_code.to_bytes(1, byteorder="little"))

        message = length_bytes + code_bytes
        crc = calculate_crc(message)
        packet = header + direction + message
        packet.append(crc)
        self._connection.send(packet)

        try:
            data = self.__response()
            return data
        except:
            print("Data not recieved.")

    def __response(self):
        """Recieves the OUT packages."""
        while True:
            header = struct.unpack("c", self._connection.recv(1))[0]
            if header.decode("utf-8") == "$":
                header_m = struct.unpack("c", self._connection.recv(1))[0]

                if header_m.decode("utf-8") == "M":
                    direction = struct.unpack("c", self._connection.recv(1))[0]

                    if direction.decode("utf-8") == ">":
                        size = struct.unpack("B", self._connection.recv(1))[0]
                        code = struct.unpack("B", self._connection.recv(1))[0]

                        if size == self.__msg_length and code == self.__msg_code:
                            data = self._connection.recv(6)
                            crc = self._connection.recv(1)
                            temp = struct.unpack("<ih", data)

                            alt = temp[0] / 100
                            vatio = temp[1]

                            alt_data = AltitudeData(alt, vatio)
                            return alt_data
