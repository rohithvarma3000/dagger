import struct
import time
from dagger.utils import get_direction_out_bytes, get_header_bytes, calculate_crc


class SetAttitude:
    
    __msg_code = 108 
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection
        self.attitude = []

    def _request(self):
        """Requests the OUT package."""
        header  = get_header_bytes()
        direction = get_direction_out_bytes()

        code_bytes = bytearray(SetAttitude.__msg_code.to_bytes(1, byteorder="little"))
        crc = calculate_crc(code_bytes)
        packet =  header + direction + code_bytes
        packet.append(crc)
        self._connection.send(packet)
        try:
            start = time.time()
            status = self._response(start)
            print(self.attitude)
        except:
            print("Data not recieved.")


    def _response(self, start):
        """Recieves the OUT packages."""
        
        while True:
            header = self._connection.recv(2).decode('utf-8')
            if header == '$':
                header =  header + self._connection.recv(self.__msg_length).decode('utf-8')
                break
        
        code = struct.unpack('<b', self._connection.recv(1))
        datalength = struct.unpack('<b',self._connection.recv(1))[0]
        data = self._connection.recv(datalength)
        temp = struct.unpack('<'+'h'*int(datalength/2),data)
        elapsed = time.time() - start
        self.attitude['roll']=float(temp[0]/10.0)
        self.attitude['pitch']=float(temp[1]/10.0)
        self.attitude['yaw']=float(temp[2])
        self.attitude['elapsed']=round(elapsed,3)
        self.attitude['timestamp']="%0.2f" % (time.time(),) 
        return True