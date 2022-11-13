import commands2
import wpilib

#import autonomous
#import command
#import config
#import constants
#import robot_systems
#import sensors
#import subsystem
#import utils
from oi.OI import OI

from subsystem import Drivetrain

class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain = Drivetrain()

    def autonomousPeriodic(self):
        self.drivetrain.drive_motor_1.set_raw_output(.5)
        self.drivetrain.turn_motor_1.set_raw_output(.1)

        self.drivetrain.drive_motor_2.set_raw_output(.5)
        self.drivetrain.turn_motor_2.set_raw_output(.1)

        self.drivetrain.drive_motor_3.set_raw_output(.5)
        self.drivetrain.turn_motor_3.set_raw_output(.1)

        self.drivetrain.drive_motor_4.set_raw_output(.5)
        self.drivetrain.turn_motor_4.set_raw_output(.1)
    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
