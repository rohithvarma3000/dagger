from dagger.utils import get_direction_out_bytes, get_header_bytes, calculate_crc


class SetAltitude:
    
    __msg_code = 109 
    __msg_length = 6

    def __init__(self, connection):
        self._connection = connection
        self.altitude=0
        self.vario=0


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
            self._response()
            print(self.altitude,self.vario)
        except:
            print("Data not recieved/some error occured")
    
    def _response(self): #function for parsing the response
        header=self._connection.recv(2).decode('utf-8')
        direction=self._connection.recv(1).decode('utf-8')
        length=self._connection.recv(1).decode('utf-8')
        code=self._connection.recv(1).decode('utf-8')
        self.altitude=int(self._connection.recv(4).decode('utf-8'))
        self.vario=int(self._connection.recv(2).decode('utf-8'))