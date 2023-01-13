import struct
import time
from dagger.utils import get_direction_in_bytes, get_header_bytes, calculate_crc, ZERO


class AnalogData:
    def __init__(self, vbat, int_power_meter_sum, rssi, amperage):
        self.vbat = vbat
        self.int_power_meter_sum = int_power_meter_sum
        self.rssi = rssi
        self.amperage = amperage
        self.timestamp = time.time()


class Analog:

    __msg_code = 110
    __msg_length = 7

    def __init__(self, connection):
        self._connection = connection
        self.analog = {}

    def get_analog_data(self):
        """Requests the OUT package."""
        header = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(Analog.__msg_code.to_bytes(1, byteorder="little"))

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
                            data = self._connection.recv(size)
                            temp = struct.unpack("<BHHH", data)

                            vbat = float(temp[0])
                            int_power_meter_sum = float(temp[1])
                            rssi = float(temp[2])
                            amperage = float(temp[3])

                            analog_data = AnalogData(
                                vbat, int_power_meter_sum, rssi, amperage
                            )
                            return analog_data
