import struct
import time
from dagger.utils import get_direction_in_bytes, get_header_bytes, calculate_crc, ZERO


class Attitude:

    __msg_code = 108
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection
        self.attitude = {}

    def attitude_request(self):
        """Requests the OUT package."""
        header = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(Attitude.__msg_code.to_bytes(1, byteorder="little"))

        message = length_bytes + code_bytes
        crc = calculate_crc(message)
        packet = header + direction + message
        packet.append(crc)
        self._connection.send(packet)

        try:
            start = time.time()
            status = self.attitude_response(start)
            print(self.attitude)
        except:
            print("Data not recieved.")

    def attitude_response(self, start):
        """Recieves the OUT packages."""
        while True:
            header = struct.unpack("c", self._connection.recv(1))[0]
            if header.decode("utf-8") == "$":
                print(header.decode("utf-8"))
                header_m = struct.unpack("c", self._connection.recv(1))[0]
                print(header_m)
                if header_m.decode("utf-8") == "M":
                    direction = struct.unpack("c", self._connection.recv(1))[0]
                    print(direction)
                    if direction.decode("utf-8") == ">":
                        size = struct.unpack("B", self._connection.recv(1))[0]
                        code = struct.unpack("B", self._connection.recv(1))[0]
                        print(size, code)
                        if size == 6 and code == 108:
                            data = self._connection.recv(6)
                            temp = struct.unpack("<hhh", data)
                            elapsed = time.time() - start
                            self.attitude["roll"] = float(temp[0])
                            self.attitude["pitch"] = float(temp[1])
                            self.attitude["yaw"] = float(temp[2])
                            self.attitude["elapsed"] = round(elapsed, 3)
                            self.attitude["timestamp"] = "%0.2f" % (time.time(),)
                            break

        return True
