from robotpy_toolkit_7407.motors.rev_motors import SparkMax, SparkMaxConfig
import rev
import wpilib
import math
from wpilib import SmartDashboard

TURN_CONFIG = SparkMaxConfig(
    0.2, 0, 0.003, 0.00015, (-0.5, 0.5), rev.CANSparkMax.IdleMode.kBrake
)
MOVE_CONFIG = SparkMaxConfig(
    0.00005, 0, 0.0004, 0.00017, idle_mode=rev.CANSparkMax.IdleMode.kBrake
)

class SwerveNode:
    def __init__(self, drive_can: int, turn_can:int, encoder_port: int, encoder_zero: int, drive_reversed: bool = False, turn_reversed: bool = False, ):
        self.drive_motor = SparkMax(can_id = drive_can, config = MOVE_CONFIG, )
        self.drive_motor.init()

        self.turn_motor = SparkMax(can_id = turn_can, config=TURN_CONFIG)
        self.turn_motor.init()
        
        self.drive_reversed = drive_reversed
        self.turn_reversed = turn_reversed

        self.encoder_port = encoder_port
        self.encoder_zero = encoder_zero
        self.offset = 0
        

    def turn(self, angle):
        if self.turn_reversed:
            self.turn_motor.set_target_position(-1 * angle * 88/360)
        else:
            self.turn_motor.set_target_position(angle / 88.4848/360)
        
    def set_speed(self, speed):
        if self.drive_reversed:
            self.drive_motor.set_raw_output(-1 * speed)
        else:
            self.drive_motor.set_raw_output(speed)

    def zero_turn(self):
        encoder = wpilib.AnalogEncoder(self.encoder_port)
        encoder_val = encoder.getAbsolutePosition()
        encoder_offset = encoder_val - self.encoder_zero
        motor_position = self.turn_motor.get_sensor_position()
        motor_zerod_position =  encoder_offset * 88.4848
        wheel_position = motor_position / 88.4848
        self.turn_motor.set_sensor_position(motor_zerod_position)
        SmartDashboard.putNumber(f"Motor Position Encoder {self.turn_motor._can_id}", wheel_position)
        SmartDashboard.putNumber(f"Encoder offset {self.turn_motor._can_id}", encoder_offset)
        SmartDashboard.putNumber(f"Motor Position {self.turn_motor._can_id}", motor_position)

class Drivetrain:
    def __init__(self):
        self.swerve_node_1 = SwerveNode(1, 2, 0, 0.581, drive_reversed=True)
        self.swerve_node_2 = SwerveNode(3, 4, 3, 0.415)
        self.swerve_node_3 = SwerveNode(5, 6, 2, 0.580,  turn_reversed=True)
        self.swerve_node_4 = SwerveNode(7, 8, 1, 0.994, turn_reversed=True, drive_reversed=True)

    def turn(self, angle):
        self.swerve_node_1.turn(angle)
        self.swerve_node_2.turn(angle)
        self.swerve_node_3.turn(angle)
        self.swerve_node_4.turn(angle)
    
    def zero_turn(self):
        self.swerve_node_1.zero_turn()
        self.swerve_node_2.zero_turn()
        self.swerve_node_3.zero_turn()
        self.swerve_node_4.zero_turn()

    def drive(self, speed):
        self.swerve_node_1.set_speed(speed)
        self.swerve_node_2.set_speed(speed)
        self.swerve_node_3.set_speed(speed)
        self.swerve_node_4.set_speed(speed)
    
    def tankdrive(self, leftspeed, rightspeed):
        if abs(leftspeed) > .15:
            self.swerve_node_1.set_speed(leftspeed)
            self.swerve_node_4.set_speed(leftspeed)
        else:
            self.swerve_node_1.set_speed(0)
            self.swerve_node_4.set_speed(0)
        if abs(rightspeed) > .15:
            self.swerve_node_2.set_speed(-rightspeed)
            self.swerve_node_3.set_speed(-rightspeed)
        else:
            self.swerve_node_2.set_speed(0)
            self.swerve_node_3.set_speed(0)