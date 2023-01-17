from dagger.set_command import SetCommand
from dagger.set_raw_rc import SetRawRC


class PlutoControl(SetRawRC, SetCommand):

    def __init__(self, connection):
        super().__init__(connection=connection)
