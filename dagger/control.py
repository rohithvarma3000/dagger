from dagger.set_command import SetCommand
from dagger.set_raw_rc import SetRawRC
from dagger.set_command import CmdType


class PlutoControl(SetRawRC, SetCommand):

    def __init__(self, connection):
        """Defines the class variable."""
        super().__init__(connection=connection)
        self.connection = connection

    def take_off(self):
        self.disarm_drone()
        self.box_arm()
        self.command(CmdType.TAKE_OFF)

    def land(self):
        self.command(CmdType.land)

    def pitch_forward(self):
        self.set_pitch(1600)

    def pitch_backward(self):
        self.set_pitch(1400)

    def roll_left(self):
        self.set_roll(1400)

    def roll_right(self):
        self.set_roll(1600)

    def left_yaw(self):
        self.set_yaw(1200)

    def right_yaw(self):
        self.set_yaw(1800)
