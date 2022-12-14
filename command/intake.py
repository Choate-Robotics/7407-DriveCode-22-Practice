import time

import commands2
from robotpy_toolkit_7407.command import SubsystemCommand

from oi.keymap import Keymap
from robot_systems import Pneumatics
from subsystem import Intake

class LeftDown(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def execute(self):
        Pneumatics.left_intake.down()

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False

class LeftUp(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def execute(self):
        Pneumatics.left_intake.up()

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False

class RightDown(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def execute(self):
        Pneumatics.right_intake.down()

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False

class RightUp(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def execute(self):
        Pneumatics.right_intake.up()

    def end(self, interrupted=False):
        ...

    def isFinished(self):
        return False
