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
        self.left_motors[0].set_raw_output(-power)
        self.left_motors[1].set_raw_output(-power)

    def set_right(self, power):
        self.right_motors[0].set_raw_output(power)
        self.right_motors[1].set_raw_output(power)

    def set_all(self, power):
        self.set_right(power)
        self.set_left(power)

    def turn(self, power):  # + turns left, - turns right
        self.set_left(-power)
        self.set_right(power)

    def turn_while_drive(self, forward, turn):   # turn: + turns right, - turns left
        left_power = forward + turn
        right_power = forward - turn
        if abs(left_power) >= 1 and abs(left_power) > abs(right_power):
            difference = abs(left_power - right_power)
            right_power = 1 - difference
            left_power = 1
        elif abs(right_power) >= 1:
            difference = abs(right_power - left_power)
            right_power = 1 - difference
            left_power = 1
        self.set_left(left_power)
        self.set_right(right_power)

