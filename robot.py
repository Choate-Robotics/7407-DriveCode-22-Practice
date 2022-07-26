import commands2
import wpilib
from robotpy_toolkit_7407.utils import logger

import autonomous
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI


class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__(constants.period)

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        wpilib.LiveWindow.disableAllTelemetry()
        logger.Color = logger.NoColor

        logger.info("Initializing robot...", "[Robot]")

        robot_systems.Robot.intake.init()

        OI.init()
        OI.map_controls()

        commands2.CommandScheduler.getInstance().setPeriod(constants.period)

        logger.info("Robot initialized!", "[Robot]")

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    def teleopPeriodic(self):
        logger.info(
            f"Intake Speeds: {robot_systems.Robot.intake.get_intake_speeds()}",
            "[ROBOT<-INTAKE]",
        )

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
