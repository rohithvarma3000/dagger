from dagger.altitude import Altitude
from dagger.acc_calibration import AccCalibration
from dagger.mag_calibration import MagCalibration
from dagger.raw_imu import RawIMU


class PlutoControl(Altitude, AccCalibration, MagCalibration, RawIMU):
    def __init__(self, connection):
        super().__init__(connection=connection)
