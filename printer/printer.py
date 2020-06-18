from pylgbst import *
from pylgbst.comms.cpygatt import GattoolConnection
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor
from common.resetablemovehub import ResetableMoveHub
from common.capitals import *
import argparse
import logging

logger = logging.getLogger("printer")

class boostprinter(object):
    PEN_DOWN_UP_TIME = 1.5
    PEN_DOWN_UP_SPEED = 1.0
    BASE_TIMED = 1.0
    X_BASE_SPEED = 0.175
    Y_BASE_SPEED = 0.07

    # base on angle moved
    BASE_SPEED_ANGLE = 0.1
    BASE_ANGLE = 180

    _pen_down = False

    def __init__(self):
        conn = GattoolConnection()
        conn.connect('00:16:53:A9:94:DF')
        self.hub = ResetableMoveHub(conn)

    def down_pen(self, bforce=False):
        if self._pen_down is True and bforce is False:
            return
        self._pen_down = True
        pen_motor = self._get_motor_for_pen()
        if pen_motor is not None:
            pen_motor.timed(self.PEN_DOWN_UP_TIME, self.PEN_DOWN_UP_SPEED)

    def up_pen(self, bforce=False):
        if self._pen_down is False and bforce is False:
            return
        self._pen_down = False
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

        logger.error("line {}".format(line_xy))
        if line_xy[1] == 0 and line_xy[2] == 0:
            pass
        elif line_xy[1] != 0 and line_xy[2] == 0:
            direction_x = 1
            if line_xy[1] < 0:
                direction_x = -1
            time_x = line_xy[1] * self.BASE_TIMED / 2
            logger.error("line X time {} speed {}".format(abs(time_x), self.X_BASE_SPEED * direction_x))
            self.hub.motor_A.timed(abs(time_x), self.X_BASE_SPEED * direction_x)
        elif line_xy[1] == 0 and line_xy[2] != 0:
            time_y = line_xy[2] * self.BASE_TIMED / 2
            direction_y = 1
            if line_xy[2] < 0:
                direction_y = -1
            logger.error("line Y time {} speed {}".format(abs(time_y), self.Y_BASE_SPEED * direction_y))
            self.hub.motor_B.timed(abs(time_y), self.Y_BASE_SPEED * direction_y)
        else:
            direction_x = 1
            direction_y = 1
            if line_xy[1] < 0:
                direction_x = -1
            if line_xy[2] < 0:
                direction_y = -1
            ratio = 1
            speed_x = self.X_BASE_SPEED
            speed_y = self.Y_BASE_SPEED
            time_xy = line_xy[1] * self.BASE_TIMED / 2
            speed_x = self.X_BASE_SPEED * direction_x
            speed_y = self.Y_BASE_SPEED * direction_y

            logger.error("line XY time {} speedx {} speedy {}".format(abs(time_xy), speed_x, speed_y))
            self.hub.motor_AB.timed(abs(time_xy), speed_x, speed_y)

    def line_angle(self, line_xy):
        if line_xy[0] == 1:
            self.down_pen()
        elif line_xy[0] == 0:
            self.up_pen()
        else:
            pass

        logger.error("line {}".format(line_xy))
        if line_xy[1] == 0 and line_xy[2] == 0:
            pass
        elif line_xy[1] != 0 and line_xy[2] == 0:
            direction_x = 1
            if line_xy[1] < 0:
                direction_x = -1
            time_x = line_xy[1] * self.BASE_ANGLE
            logger.error("line X angle {} speed {}".format(abs(time_x), self.X_BASE_SPEED * direction_x))
            self.hub.motor_A.angled(abs(time_x), self.BASE_SPEED_ANGLE * direction_x)
        elif line_xy[1] == 0 and line_xy[2] != 0:
            direction_y = 1
            if line_xy[2] < 0:
                direction_y = -1
            time_y = line_xy[2] * self.BASE_ANGLE
            logger.error("line Y angle {} speed {}".format(abs(time_y), self.Y_BASE_SPEED * direction_y))
            self.hub.motor_B.angled(abs(time_y), self.BASE_SPEED_ANGLE * direction_y)
        else:
            direction_x = 1
            direction_y = 1
            if line_xy[1] < 0:
                direction_x = -1
            if line_xy[2] < 0:
                direction_y = -1
            ratio = 1
            speed_x = self.X_BASE_SPEED
            speed_y = self.Y_BASE_SPEED
            time_xy = line_xy[1] * self.BASE_ANGLE
            speed_x = self.BASE_SPEED_ANGLE * direction_x
            speed_y = self.BASE_SPEED_ANGLE * direction_y

            logger.error("line XY angle {} speedx {} speedy {}".format(abs(time_xy), speed_x, speed_y))
            self.hub.motor_AB.angled(abs(time_xy), speed_x, speed_y)

    def _space(self, space):
        self.up_pen()
        self.hub.motor_A.angled(space * self.BASE_ANGLE, self.BASE_SPEED_ANGLE)

    def print_cap(self, cap):
        logger.error("print letter {}".format(cap))
        data = capitals[cap]()
        space = 1
        if data is not None:
            for lineXY in data:
                if abs(lineXY[1]) > space:
                    space = abs(lineXY[1])
                self.line_angle(lineXY)
            self._space(space + 0.5)


    def _get_motor_for_pen(self):
        if isinstance(self.hub.port_C, EncodedMotor):
            return self.hub.port_C
        if isinstance(self.hub.port_D, EncodedMotor):
            return self.hub.port_D
        return None

    def fresh_xy(self):
        printer.test_x_move()
        printer.test_y_move()
        printer.test_x_move_back()
        printer.test_y_move_back()

    def fresh_xy_angle(self):
        printer.test_x_move_angle()
        printer.test_y_move_angle()
        printer.test_x_move_back_angle()
        printer.test_y_move_back_angle()

    def test_x_move(self):
        self.hub.motor_A.timed(self.BASE_TIMED, self.X_BASE_SPEED)

    def test_y_move(self):
        self.hub.motor_B.timed(self.BASE_TIMED, self.Y_BASE_SPEED)

    def test_x_move_back(self):
        self.hub.motor_A.timed(self.BASE_TIMED, -self.X_BASE_SPEED)

    def test_y_move_back(self):
        self.hub.motor_B.timed(self.BASE_TIMED, -self.Y_BASE_SPEED)

    def test_x_move_angle(self):
        self.hub.motor_A.angled(self.BASE_ANGLE, self.BASE_SPEED_ANGLE)

    def test_y_move_angle(self):
        self.hub.motor_B.angled(self.BASE_ANGLE, self.BASE_SPEED_ANGLE)

    def test_x_move_back_angle(self):
        self.hub.motor_A.angled(self.BASE_ANGLE, -self.BASE_SPEED_ANGLE)

    def test_y_move_back_angle(self):
        self.hub.motor_B.angled(self.BASE_ANGLE, -self.BASE_SPEED_ANGLE)

    def test_xy_move_dif(self):
        self.hub.motor_AB.timed(self.BASE_TIMED, self.X_BASE_SPEED, self.Y_BASE_SPEED)

    def test_xy_move_back_dif(self):
        self.hub.motor_AB.timed(self.BASE_TIMED, -self.X_BASE_SPEED, -self.Y_BASE_SPEED)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--strprint', '-s', help='string for print')
args = arg_parser.parse_args()

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    printer = boostprinter()

    try:
        printer.fresh_xy_angle()
        string_print = ""
        if args.strprint is not None:
            if args.strprint != "":
                string_print = args.strprint
                string_print.upper()

        if string_print != "":
            caps_list = list(string_print)
            caps_list.reverse()
            for cap in caps_list:
                printer.print_cap(cap)
    finally:
        printer.up_pen()


