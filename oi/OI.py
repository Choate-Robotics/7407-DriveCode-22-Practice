from robotpy_toolkit_7407.utils import logger

import command
from oi.keymap import Keymap
from robot_systems import Robot


class OI:
    @staticmethod
    def init() -> None:
        logger.info("Initializing OI...", "[OI]")

    @staticmethod
    def map_controls():
        logger.info("Mapping controls...", "[OI]")

        Keymap.Intake.INCREASE_SPEED.whenPressed(
            command.IntakeChangeSpeed(Robot.intake, True)
        )
        Keymap.Intake.DECREASE_SPEED.whenPressed(
            command.IntakeChangeSpeed(Robot.intake, False)
        )
        Keymap.Intake.STOP_MOTORS.whenPressed(command.IntakeStop(Robot.intake))

        logger.info("Controls mapped!", "[OI]")
