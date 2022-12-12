import commands2
import ctre
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

from subsystem import Drivetrain


class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()
        commands2.CommandScheduler.getInstance().setPeriod(.03)
    
    def robotPeriodic(self) -> None:

        commands2.CommandScheduler.getInstance().run()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        commands2.CommandScheduler.getInstance().schedule(
            command.TankDrive(subsystem.Drivetrain)
        )

    def teleopPeriodic(self):
        ...

    def autonomousInit(self):
        self.drivetrain = Drivetrain()
        self.drivetrain.init()
        self.drivetrain.setDirection()

    def autonomousPeriodic(self):
        self.drivetrain.setLeftSpeed(0.25)
        self.drivetrain.setRightSpeed(-0.25)

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
