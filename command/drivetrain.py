import time

import commands2
from robotpy_toolkit_7407.command import SubsystemCommand

from oi.keymap import Keymap
from robot_systems import Robot
from subsystem import Drivetrain


class MoveSideways(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        ...

    def execute(self):
        left_speed = Keymap.Drivetrain.LEFT_WHEELS_SPEED.value
        right_speed = Keymap.Drivetrain.RIGHT_WHEELS_SPEED.value
        Robot.drivetrain.n1.set_angle(90)
        Robot.drivetrain.n2.set_angle(90)
        Robot.drivetrain.n3.set_angle(90)
        Robot.drivetrain.n4.set_angle(90)

        Robot.drivetrain.n1.set_speed(left_speed)
        Robot.drivetrain.n2.set_speed(-right_speed)
        Robot.drivetrain.n3.set_speed(right_speed)
        Robot.drivetrain.n4.set_speed(-left_speed)

        print("moving sideways")

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False


class TankDrive(SubsystemCommand[Drivetrain]):
    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        ...

    def execute(self):
        left_speed = Keymap.Drivetrain.LEFT_WHEELS_SPEED.value
        right_speed = Keymap.Drivetrain.RIGHT_WHEELS_SPEED.value
        Robot.drivetrain.n1.set_angle(0)
        Robot.drivetrain.n2.set_angle(0)
        Robot.drivetrain.n3.set_angle(0)
        Robot.drivetrain.n4.set_angle(0)

        Robot.drivetrain.n1.set_speed(-left_speed)
        Robot.drivetrain.n2.set_speed(left_speed)
        Robot.drivetrain.n3.set_speed(-right_speed)
        Robot.drivetrain.n4.set_speed(right_speed)

        print("tankdrive running")

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False
