from robotpy_toolkit_7407.command import SubsystemCommand

import config
from subsystem import Intake


class IntakeChangeSpeed(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake, increment: bool):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.increment = increment

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        if self.increment:
            self.subsystem.desired_power += config.INTAKE.speed_increment
        else:
            self.subsystem.desired_power -= config.INTAKE.speed_increment

        self.subsystem.set_intake_turn_power(self.subsystem.desired_power)

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        pass


class IntakeStop(SubsystemCommand[Intake]):
    def __init__(self, subsystem: Intake):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        self.subsystem.stop()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        pass
