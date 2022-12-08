import commands2
from oi.OI import OI
from oi.keymap import Keymap
import wpilib
import robot_systems
from robotpy_toolkit_7407.command import SubsystemCommand
import subsystem


class TankDrive(SubsystemCommand[subsystem.Drivetrain]):

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        forward = Keymap.Drivetrain.left_joy_forward.value if abs(Keymap.Drivetrain.left_joy_forward.value) > .15 else 0
        turn = Keymap.Drivetrain.left_joy_horizontal.value if abs(Keymap.Drivetrain.left_joy_horizontal.value) \
                                                              > .15 else 0
        robot_systems.Robot.drivetrain.turn_while_drive(forward, turn)
        pass

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self):
        return False

    def runsWhenDisabled(self):
        return False
