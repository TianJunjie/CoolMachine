from pylgbst import *
from pylgbst.comms.cpygatt import GattoolConnection
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor
from common.resetablemovehub import ResetableMoveHub


class boostprinter(object):
    PEN_DOWN_UP_TIME = 1.5
    PEN_DOWN_UP_SPEED = 1.0

    def __init__(self):
        conn = GattoolConnection()
        conn.connect('00:16:53:A9:94:DF')
        self.hub = ResetableMoveHub(conn)

    def down_pen(self):
        pen_motor = self._get_motor_for_pen()
        if pen_motor is not None:
            pen_motor.timed(self.PEN_DOWN_UP_TIME, self.PEN_DOWN_UP_SPEED)

    def up_pen(self):
        pen_motor = self._get_motor_for_pen()
        if pen_motor is not None:
            pen_motor.timed(self.PEN_DOWN_UP_TIME, -self.PEN_DOWN_UP_SPEED)

    def line(self):
        pass

    def _get_motor_for_pen(self):
        if isinstance(self.hub.port_C, EncodedMotor):
            return self.hub.port_C
        if isinstance(self.hub.port_D, EncodedMotor):
            return self.hub.port_D
        return None

    def test_x_move(self):
        self.hub.motor_A.angled(360, 0.1)

    def test_y_move(self):
        self.hub.motor_B.angled(180, 0.1)

    def test_x_move_back(self):
        self.hub.motor_A.angled(360, -0.1)

    def test_y_move_back(self):
        self.hub.motor_B.angled(180, -0.1)


if __name__ == '__main__':
    printer = boostprinter()
    printer.down_pen()

    for i in range(0, 5):
        printer.test_x_move()
        printer.test_y_move()
        printer.test_x_move_back()
        printer.test_y_move_back()
        printer.up_pen()
        printer.test_x_move()
        printer.down_pen()
    printer.up_pen()
