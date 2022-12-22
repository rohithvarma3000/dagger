import enum
from dagger.utils import get_header_bytes, get_direction_in_bytes, calculate_crc


class CmdType(enum.Enum):
    TAKE_OFF = 1
    LAND = 2
    BACK_FLIP = 3
    FRONT_FLIP = 4
    RIGHT_FLIP = 5
    LEFT_FLIP = 6


class SetCommand:
    __msg_length = 2
    __msg_code = 217

    def __init__(self, connection):
        self._connection = connection
        self.command = 0

    def command(self, cmd):
        self.command = cmd.value
        self._send()

    def _send(self):
        header = get_header_bytes()
        direction = get_direction_in_bytes()
        length_bytes = bytearray(SetCommand.__msg_length.to_bytes(1))
        code_bytes = bytearray(SetCommand.__msg_code.to_bytes(1))
        payload = bytearray(self.command.to_bytes(2, byte_order="little"))

        message = bytearray().append(length_bytes, code_bytes, payload)
        crc = calculate_crc(message)
        packet = bytearray().append(header, direction, message, crc)
        self._connection.send(packet)
