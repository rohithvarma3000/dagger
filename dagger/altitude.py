import struct
import time
from dagger.utils import get_direction_out_bytes, get_header_bytes, calculate_crc


class SetAltitude:
    
    __msg_code = 109 
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection
        self.altitude = []

    def _request(self): #function for requesting the out packet
        header  = get_header_bytes()
        direction = get_direction_in_bytes() #Requesting the out packet using an in direction as mentioned in docs
        length_bytes = bytearray(SetAltitude.__msg_length.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(SetAltitude.__msg_code.to_bytes(1, byteorder="little"))
        message=length_bytes+code_bytes #no payload data
        crc = calculate_crc(message)
        packet =  header + direction + message
        packet.append(crc)
        self._connection.send(packet)

        try:
            start = time.time()
            status = self._response(start)
            print(self.altitude)
        except:
            print("Data not recieved.")