import commands2
import wpilib
from wpilib import DoubleSolenoid

from robotpy_toolkit_7407.motors.ctre_motors import TalonFX, TalonConfig

class Intake(commands2.Subsystem):
    def __init__(self, can_id: int, module: int, forward_channel: int, reverse_channel: int):
        super().__init__()

        self.motor = TalonFX(can_id)
        self.piston = DoubleSolenoid(module, wpilib.PneumaticsModuleType.REVPH, forward_channel, reverse_channel)

        self.motor.init()

    def down(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def up(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)
