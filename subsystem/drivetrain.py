from robotpy_toolkit_7407.motors.rev_motors import SparkMax

class Drivetrain:
    def __init__(self):
        self.left_motors = [SparkMax(1), SparkMax(3, inverted=False)]
        self.right_motors = [SparkMax(5, inverted=False), SparkMax(7)]
        self.left_motors[0].init()
        self.left_motors[1].init()
        self.right_motors[0].init()
        self.right_motors[1].init()

    def set_left(self, power):
        self.left_motors[0].set_raw_output(power)
        self.left_motors[1].set_raw_output(power)

    def set_right(self, power):
        self.right_motors[0].set_raw_output(power)
        self.right_motors[1].set_raw_output(power)

    def set_all(self, power):
        self.set_right(power)
        self.set_left(power)
