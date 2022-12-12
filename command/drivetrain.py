import commands2
from oi.OI import OI
from oi.keymap import Keymap
from robot_systems import Robot
from robotpy_toolkit_7407.command import SubsystemCommand
import subsystem

class TankDrive (commands2.CommandBase):
    def __init__(self, subsystem: subsystem.Drivetrain):
        super().__init__()
        self.subsystem = subsystem

    def initialize(self):
        Robot.drivetrain.setDirection()

    def execute(self):
        Robot.drivetrain.setLeftSpeed(Keymap.Drivetrain.DRIVE_LEFT.value)
        Robot.drivetrain.setRightSpeed(Keymap.Drivetrain.DRIVE_RIGHT.value)

    def isFinished(self):
        return False

    def end():
        ...