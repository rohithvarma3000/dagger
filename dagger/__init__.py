import sys  
from dagger.connect import PlutoConnection
from dagger.set_command import SetCommand, CmdType
from dagger.set_raw_rc import SetRawRC
from dagger.altitude import SetAltitude
from dagger.attitude import SetAttitude
from dagger.analog  import GetAnalog
from dagger.acc_calibration import AccCalibration
from dagger.mag_calibration import MagCalibration
from dagger.raw_imu import RawIMU

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
