from robotpy_toolkit_7407.motors.rev_motors import SparkMax

class Drivetrain:
    def __init__(self):
        self.drive_motor_1 = SparkMax(can_id=1)
        self.turn_motor_1 = SparkMax(can_id=2)
        self.drive_motor_1.init()
        self.turn_motor_1.init()

        self.drive_motor_2 = SparkMax(can_id=3)
        self.turn_motor_2 = SparkMax(can_id=4)
        self.drive_motor_2.init()
        self.turn_motor_2.init()

        self.drive_motor_3 = SparkMax(can_id=5)
        self.turn_motor_3 = SparkMax(can_id=6)
        self.drive_motor_3.init()
        self.turn_motor_3.init()
        
        self.drive_motor_4 = SparkMax(can_id=7) 
        self.turn_motor_4 = SparkMax(can_id=8)
        self.drive_motor_4.init()
        self.turn_motor_4.init()