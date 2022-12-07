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
        left_power = Keymap.Drivetrain.left_joy.value if abs(Keymap.Drivetrain.left_joy.value) > .15 else 0
        right_power = Keymap.Drivetrain.right_joy.value if abs(Keymap.Drivetrain.right_joy.value) > .15 else 0
        robot_systems.Robot.drivetrain.set_left(left_power)
        robot_systems.Robot.drivetrain.set_right(right_power)
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
