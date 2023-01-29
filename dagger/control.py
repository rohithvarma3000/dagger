"""Controls for the Pluto Drone."""
from dagger.set_command import SetCommand
from dagger.set_raw_rc import SetRawRC
from dagger.set_command import CmdType


class PlutoControl(SetRawRC, SetCommand):
    """Controls for the Pluto Drone.

    Parameters
    ----------
    connection : PlutoConnection
        Pluto connection object for communicating with ``Pluto``.

    Examples
    --------
    >>> t = dagger.PlutoConnection()
    >>> t.connect(('Pluto_IP', Pluto_port))
    >>> control = dagger.PlutoControl(t)
    """

    def __init__(self, connection):
        """Defines the class variable."""
        super().__init__(connection=connection)
        self.connection = connection

    def take_off(self):
        """Take off command for Pluto.

        Examples
        --------
        >>> control.take_off()
        """
        self.disarm_drone()
        self.box_arm()
        self.command(CmdType.TAKE_OFF)

    def land(self):
        """Landing command for Pluto.

        Examples
        --------
        >>> control.land()
        """

        self.command(CmdType.land)

    def pitch_forward(self):
        """Forward Pitch command for Pluto.

        Examples
        --------
        >>> control.pitch_forward()
        """
        self.set_pitch(1600)

    def pitch_backward(self):
        """Backward Pitch command for Pluto.

        Examples
        --------
        >>> control.pitch_backward()
        """
        self.set_pitch(1400)

    def roll_left(self):
        """Left Roll command for Pluto.

        Examples
        --------
        >>> control.roll_left()
        """
        self.set_roll(1400)

    def roll_right(self):
        """Right Roll command for Pluto.

        Examples
        --------
        >>> control.roll_right()
        """
        self.set_roll(1600)

    def left_yaw(self):
        """Left Yaw command for Pluto.

        Examples
        --------
        >>> control.left_yaw()
        """
        self.set_yaw(1200)

    def right_yaw(self):
        """Right Yaw command for Pluto.

        Examples
        --------
        >>> control.right_yaw()
        """
        self.set_yaw(1800)
