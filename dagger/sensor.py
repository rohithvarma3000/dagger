from dagger.altitude import Altitude
from dagger.acc_calibration import AccCalibration
from dagger.mag_calibration import MagCalibration
from dagger.raw_imu import RawIMU
from dagger.analog import Analog
from dagger.attitude import Attitude


class PlutoSensor():

    def __init__(self, connection):
        self.Altitude = Altitude(connection)
        self.AccCalibration = AccCalibration(connection)
        self.MagCalibration = MagCalibration(connection)
        self.RawIMU = RawIMU(connection)
        self.Analog = Analog(connection)
        self.Attitude = Attitude(connection)

    def get_altitude_data(self):
        return self.Altitude.get_altitude_data()

    def get_analog_data(self):
        return self.Altitude.get_analog_data()

    def get_attitude_data(self):
        return self.Altitude.get_attitude_data()

    def get_raw_imu(self):
        return self.RawIMU.get_raw_imu()

    def mag_calibration(self):
        return self.MagCalibration.mag_calibration()

    def acc_calibartion(self):
        return self.AccCalibration.acc_calibartion()
