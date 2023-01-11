import struct
from dagger.utils import get_header_bytes, get_direction_in_bytes, calculate_crc, ZERO


class RawIMUData:
    def __init(self, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, mag_x, mag_y, mag_z):
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
        self.gyro_x = gyro_x
        self.gyro_y = gyro_y
        self.gyro_z = gyro_z
        self.mag_x = mag_x
        self.mag_y = mag_y
        self.mag_z = mag_z


class RawIMU:
    __msg_length = 18
    __msg_code = 102

    def __init__(self, connection):
        self._connection = connection

    def get_raw_imu(self):
        header = get_header_bytes()
        direction = get_direction_in_bytes()

        length_bytes = bytearray(ZERO.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(RawIMU.__msg_code.to_bytes(1, byteorder="little"))

        crc = calculate_crc(length_bytes + code_bytes)
        packet = header + direction + length_bytes + code_bytes
        packet.append(crc)
        self._connection.send(packet)

        data = self._connection.recv(RawIMU.__msg_length + 6)
        struct_data = struct.unpack("cccBB<H<H<H<H<H<H<H<H<HB")
        obj = RawIMUData(
            struct_data[6],
            struct_data[7],
            struct_data[8],
            struct_data[9],
            struct_data[10],
            struct_data[11],
            struct_data[12],
            struct_data[13],
            struct_data[14],
        )
        return obj
