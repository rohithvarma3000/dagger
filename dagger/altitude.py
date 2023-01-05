import struct
import time
from dagger.utils import get_direction_in_bytes, get_header_bytes, calculate_crc, ZERO


class SetAltitude:
    
    __msg_code = 109
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection
        self.altitude = {}

    def altitude_request(self):
        """Requests the OUT package."""
        header  = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(SetAltitude.__msg_code.to_bytes(1, byteorder="little"))
        
        message =  length_bytes + code_bytes
        crc = calculate_crc(message)
        packet =  header + direction + message
        packet.append(crc)
        self._connection.send(packet)

        try:
            start = time.time()
            status = self.altitude_response(start)
            print(self.altitude)
        except:
            print("Data not recieved.")


    def altitude_response(self, start):
        """Recieves the OUT packages."""
        while True:
            header = struct.unpack('c',self._connection.recv(1))[0]
            if header.decode('utf-8') == '$':
                print(header.decode('utf-8'))
                header_m = struct.unpack('c', self._connection.recv(1))[0]
                print(header_m)
                if header_m.decode('utf-8') == 'M':
                    direction = struct.unpack('c', self._connection.recv(1))[0]
                    print(direction)
                    if direction.decode('utf-8') == '>':
                        size = struct.unpack('B', self._connection.recv(1))[0]
                        code = struct.unpack('B', self._connection.recv(1))[0]
                        print(size, code)
                        if size == self.__msg_length and code == self.__msg_code:
                            data = self._connection.recv(6)
                            crc = self._connection.recv(1)
                            temp = struct.unpack('<ih',data)
                            elapsed = time.time() - start
                            self.altitude['altitude']=float(temp[0])
                            self.altitude['vatio']=float(temp[1])
                            self.altitude['elapsed']=round(elapsed,3)
                            self.altitude['timestamp']="%0.2f" % (time.time(),) 
                            break
    
        return True





            # altitude = struct.unpack("<i", self._connection.recv(4))[
            #     0
            # ]  # signed int of 4 bytes hence i
            # vario = struct.unpack("<h", self._connection.recv(2))[
            #     0
            # ]  # signed int of 2 bytes hence h
            # crc_out = struct.unpack("B", self._connection.recv(1))[0]