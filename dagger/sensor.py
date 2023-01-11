from dagger.altitude import Altitude
from dagger.acc_calibration import AccCalibration
from dagger.mag_calibration import MagCalibration
from dagger.raw_imu import RawIMU
from dagger.analog import Analog
from dagger.attitude import Attitude


class PlutoSensor(Altitude, AccCalibration, MagCalibration, RawIMU, Analog, Attitude):
    def __init__(self, connection):
        super().__init__(connection=connection)
