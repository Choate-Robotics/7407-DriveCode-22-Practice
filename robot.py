import commands2
import wpilib
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI
from oi.keymap import Keymap


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
        forward = Keymap.Drivetrain.left_joy_forward.value if abs(Keymap.Drivetrain.left_joy_forward.value) > .15 else 0
        turn = Keymap.Drivetrain.left_joy_horizontal.value if abs(Keymap.Drivetrain.left_joy_horizontal.value) \
                                                                      > .15 else 0

        robot_systems.Robot.drivetrain.turn_while_drive(forward, turn)
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
