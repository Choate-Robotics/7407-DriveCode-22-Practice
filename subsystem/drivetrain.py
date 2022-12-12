from robotpy_toolkit_7407.motors.rev_motors import SparkMax, SparkMaxConfig
import rev

TURN_CONFIG = SparkMaxConfig(

    0.2, 0, 0.003, 0.00015, (-0.5, 0.5), rev.CANSparkMax.IdleMode.kBrake

)

MOVE_CONFIG = SparkMaxConfig(

    0.00005, 0, 0.0004, 0.00017, idle_mode=rev.CANSparkMax.IdleMode.kBrake

)


class Drivetrain:
    def __init__(self):
        self.drive_motor_1 = SparkMax(can_id=1,config = MOVE_CONFIG)
        self.turn_motor_1 = SparkMax(can_id=2, config = TURN_CONFIG)
        self.drive_motor_2 = SparkMax(can_id=3, config = MOVE_CONFIG)
        self.turn_motor_2 = SparkMax(can_id=4, config = TURN_CONFIG)
        self.drive_motor_3 = SparkMax(can_id=5, config = MOVE_CONFIG)
        self.turn_motor_3 = SparkMax(can_id=6, config = TURN_CONFIG)
        self.drive_motor_4 = SparkMax(can_id=7, config = MOVE_CONFIG)
        self.turn_motor_4 = SparkMax(can_id=8, config = TURN_CONFIG)

    def init(self):
        self.drive_motor_1.init()
        self.turn_motor_1.init()
        self.drive_motor_2.init()
        self.turn_motor_2.init()
        self.drive_motor_3.init()
        self.turn_motor_3.init()
        self.drive_motor_4.init()
        self.turn_motor_4.init()
    
    def setSpeed(self, speed):
        self.drive_motor_1.set_raw_output(speed)
        self.drive_motor_2.set_raw_output(speed)
        self.drive_motor_3.set_raw_output(speed)
        self.drive_motor_4.set_raw_output(speed)
    
    def setDirection(self):
        self.turn_motor_1.set_target_position(60)
        self.turn_motor_2.set_target_position(20)
        self.turn_motor_3.set_target_position(60)
        self.turn_motor_4.set_target_position(20)
    
    def setLeftSpeed(self, speed):
        print("Left speed: ", speed)
        if (-0.15 <= speed and speed <= 0.15):
            self.drive_motor_1.set_raw_output(0)
            self.drive_motor_4.set_raw_output(0)
        else:
            self.drive_motor_1.set_raw_output(speed)
            self.drive_motor_4.set_raw_output(speed)
            
    def setRightSpeed(self, speed):
        print("Right speed:", speed)
        if (-0.15 <= speed and speed <= 0.15):
            self.drive_motor_2.set_raw_output(0)
            self.drive_motor_3.set_raw_output(0)
        else:
            self.drive_motor_2.set_raw_output(speed)
            self.drive_motor_3.set_raw_output(speed)