import dagger.set_raw_rc as set_raw_rc
import unittest
from unittest.mock import Mock


class TestSetRawRC(unittest.TestCase):
    msg_length = 16
    msg_code = 200
    roll_position = 5

    def test_roll(self):
        connection = Mock()
        rc = set_raw_rc.SetRawRC(connection)

        rc.set_roll(1500)
        packet = connection.send.call_args.args[0]

        assert chr(packet[0]) == "$"
        assert chr(packet[1]) == "M"
        assert chr(packet[2]) == "<"
        assert packet[3] == TestSetRawRC.msg_length
        assert packet[4] == TestSetRawRC.msg_code
        assert (
            int.from_bytes(
                packet[TestSetRawRC.roll_position : TestSetRawRC.roll_position + 2],
                "little",
            )
            == 1500
        )

        rc.set_roll(1800)
        packet = connection.send.call_args.args[0]
        assert (
            int.from_bytes(
                packet[TestSetRawRC.roll_position : TestSetRawRC.roll_position + 2],
                "little",
            )
            == 1800
        )

        rc.set_roll(1200)
        packet = connection.send.call_args.args[0]
        assert (
            int.from_bytes(
                packet[TestSetRawRC.roll_position : TestSetRawRC.roll_position + 2],
                "little",
            )
            == 1200
        )
