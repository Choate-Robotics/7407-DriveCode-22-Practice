import commands2
import wpilib
import math

#import autonomous
#import command
#import config
#import constants
#import robot_systems
#import sensors
#import subsystem
#import utils
from oi.OI import OI
from oi.keymap import Keymap
from subsystem import Drivetrain

class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()
        self.drivetrain = Drivetrain()

    def robotPeriodic(self) -> None:
        #self.drivetrain.zero_turn()
        pass


        

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.drivetrain.zero_turn()
        self.drivetrain.turn(90)
        self.drivetrain.tankdrive(Keymap.Drivetrain.DRIVE_LEFT.value, Keymap.Drivetrain.DRIVE_RIGHT.value)

    def autonomousInit(self):
        pass
    def autonomousPeriodic(self):
        self.drivetrain.zero()
        self.drivetrain.turn(0)
        
    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
