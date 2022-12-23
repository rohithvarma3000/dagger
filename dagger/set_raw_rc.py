from dagger.utils import get_header_bytes, get_direction_in_bytes, calculate_crc


class SetRawRC:
    __msg_length = 16
    __msg_code = 200

    def __init__(self, connection):
        self._connection = connection
        self.roll = 1500  # Roll command = 0
        self.pitch = 1500  # Pitch command = 0
        self.throttle = 1500  # Roll command = 0
        self.yaw = 1500  # Yaw command = 0
        self.aux1 = 1500  # Headfree Mode
        self.aux2 = 1000  # Developer Mode Off
        self.aux3 = 1000  # Throttle Free Mode
        self.aux4 = 1000  # DISARM Mode

    def set_roll(self, roll):
        self.roll = roll
        self._send()

    def set_pitch(self, pitch):
        self.pitch = pitch
        self._send()

    def set_throttle(self, throttle):
        self.throttle = throttle
        self._send()

    def set_yaw(self, yaw):
        self.yaw = yaw
        self._send()

    def arm_drone(self):
        self.aux4 = 1500
        self._send()

    def disarm_drone(self):
        self.aux4 = 1200
        self._send()

    def _send(self):
        header = get_header_bytes()
        direction = get_direction_in_bytes()

        length_bytes = bytearray(SetRawRC.__msg_length.to_bytes(1, byteorder="little"))
        code_bytes = bytearray(SetRawRC.__msg_code.to_bytes(1, byteorder="little"))

        roll_bytes = bytearray(self.roll.to_bytes(2, byteorder="little"))
        pitch_bytes = bytearray(self.pitch.to_bytes(2, byteorder="little"))
        throttle_bytes = bytearray(self.throttle.to_bytes(2, byteorder="little"))
        yaw_bytes = bytearray(self.yaw.to_bytes(2, byteorder="little"))

        aux1_bytes = bytearray(self.aux1.to_bytes(2, byteorder="little"))
        aux2_bytes = bytearray(self.aux2.to_bytes(2, byteorder="little"))
        aux3_bytes = bytearray(self.aux3.to_bytes(2, byteorder="little"))
        aux4_bytes = bytearray(self.aux4.to_bytes(2, byteorder="little"))

        payload = (
            roll_bytes
            + pitch_bytes
            + throttle_bytes
            + yaw_bytes
            + aux1_bytes
            + aux2_bytes
            + aux3_bytes
            + aux4_bytes
        )

        message = length_bytes + code_bytes + payload
        crc = calculate_crc(message)
        packet = header + direction + message
        packet.append(crc)
        self._connection.send(packet)
