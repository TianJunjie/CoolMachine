from pylgbst import *
from pylgbst.comms.cpygatt import GattoolConnection
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor
from common.resetablemovehub import ResetableMoveHub
from common.capitals import *


class boostprinter(object):
    PEN_DOWN_UP_TIME = 1.5
    PEN_DOWN_UP_SPEED = 1.0
    X_BASE_TIMED = 1
    Y_BASE_TIMED = 2
    BASE_SPEED = 0.1

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

    def line(self, line_xy):
        if line_xy[0] == 1:
            self.down_pen()
        elif line_xy[0] == 0:
            self.up_pen()
        else:
            pass

        direction_x = line_xy[1] / abs(line_xy[1])
        direction_y = line_xy[2] / abs(line_xy[2])
        if line_xy[1] == 0 && line_xy[2] == 0:
            pass
        elif line_xy[1] != 0 && line_xy[2] == 0:
            time_x = line_xy[1] * self.X_BASE_TIMED / 3
            self.hub.motor_A.timed(time_x, self.BASE_SPEED * direction_x)
        elif line_xy[1] == 0 && line_xy[2] != 0:
            time_y = line_xy[2] * self.Y_BASE_TIMED / 3
            self.hub.motor_A.timed(time_y, self.BASE_SPEED * direction_y)
        else:
            ratio = 1
            speed_x = self.BASE_SPEED
            speed_y = self.BASE_SPEED
            time_xy = 0
            if abs(line_xy[1]) > abs(line_xy[2]):
                ratio = abs(line_xy[1]) / abs(line_xy[2])
                speed_x = self.BASE_SPEED * ratio
                time_xy = line_xy[2] * self.Y_BASE_TIMED / 3
            else:
                ratio = abs(line_xy[2]) / abs(line_xy[1])
                speed_y = self.BASE_SPEED * ratio
                time_xy = line_xy[1] * self.X_BASE_TIMED / 3
            self.hub.motor_AB.timed(time_xy, speed_x, speed_y)


    def print_cap(self, cap):
        data = capitals[cap]()
        if data is not None:
            for lineXY in data:
                line(lineXY)

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
