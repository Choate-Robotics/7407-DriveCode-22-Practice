import commands2
import rev
from robotpy_toolkit_7407.motors.rev_motors import SparkMax, SparkMaxConfig
import wpilib

TURN_CONFIG = SparkMaxConfig(
    0.2, 0, 0.003, 0.00015, (-0.5, 0.5), rev.CANSparkMax.IdleMode.kBrake
)

MOVE_CONFIG = SparkMaxConfig(
    0.00005, 0, 0.0004, 0.00017, idle_mode=rev.CANSparkMax.IdleMode.kBrake
)

class SwerveNode:
    def __init__(self, drive_port: int, turn_port: int):
        self.drive_motor = SparkMax(drive_port, config=MOVE_CONFIG)
        self.turn_motor = SparkMax(turn_port, config=TURN_CONFIG)

        self.drive_motor.init()
        self.turn_motor.init()

    def set_speed(self, speed):
        if abs(speed) < 0.3:
            speed = 0
        self.drive_motor.set_raw_output(speed)

    def set_angle(self, angle):
        self.turn_motor.set_target_position(angle * 80/360)

class Drivetrain(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.n1 = SwerveNode(1, 2)
        self.n2 = SwerveNode(3, 4)
        self.n3 = SwerveNode(5, 6)
        self.n4 = SwerveNode(7, 8)
