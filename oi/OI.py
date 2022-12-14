from robotpy_toolkit_7407.utils import logger

from oi.keymap import Keymap
import command
import commands2
from robot_systems import Robot, Pneumatics
logger.info("Hi, I'm OI!")


class OI:
    @staticmethod
    def init() -> None:
        logger.info("Initializing OI...")

    @staticmethod
    def map_controls():

        # Keymap.Drivetrain.SIDEWAYS().whenPressed(
        #     command.MoveSideways(Robot.drivetrain)
        # )
        # Keymap.Drivetrain.TANKDRIVE().whenPressed(
        #     command.TankDrive(Robot.drivetrain)
        # )

        Keymap.Intake.LEFT_DOWN() \
            .whenPressed(command.LeftDown(Pneumatics.left_intake)) \
            .whenReleased(command.LeftUp(Pneumatics.left_intake)) \

        Keymap.Intake.RIGHT_DOWN() \
            .whenPressed(command.RightDown(Pneumatics.right_intake)) \
            .whenReleased(command.RightUp(Pneumatics.right_intake)) \
