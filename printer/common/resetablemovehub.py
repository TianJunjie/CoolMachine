from pylgbst.hub import MoveHub


class ResetableMoveHub(MoveHub):
    def __init__(self, connection=None):
        super(ResetableMoveHub, self).__init__(connection)
        self._init_peripherals_state()

    def _init_peripherals_state(self):
        self.motor_A_start_angle = 0
        self.motor_B_start_angle = 0
        self.motor_External_start_angle = 0
        self.vision_distance = 0
        self.tilt_roll = 0
        self.tilt_yaw = 0
        self.tilt_roll = 0

