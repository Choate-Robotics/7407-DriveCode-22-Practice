#import commands2
#import command
#import config
#import constants
#import robot_systems
#import sensors
#import subsystem
#import utils 
import wpilib
from oi.OI import OI
import robotpy_toolkit_7407
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
        Drivetrain = Drivetrain()
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain = Drivetrain()

    def autonomousPeriodic(self):
        self.drivetrain.drive_motor_1.set_raw_output(.5)
        self.drivetrain.drive_motor_2.set_raw_output(.5)
        self.drivetrain.drive_motor_3.set_raw_output(.5)
        self.drivetrain.drive_motor_4.set_raw_output(.5)

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
