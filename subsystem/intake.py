from robotpy_toolkit_7407 import Subsystem
from robotpy_toolkit_7407.motors import TalonConfig, TalonFX

import config
from utils.can_optimizations import optimize_normal_talon_no_sensor

_MOTOR_CFG = TalonConfig(neutral_brake=False)


class Intake(Subsystem):
    left_intake_motor: TalonFX = TalonFX(
        config.INTAKE.CAN.left_intake_motor, inverted=False, config=_MOTOR_CFG
    )
    right_intake_motor: TalonFX = TalonFX(
        config.INTAKE.CAN.right_intake_motor, inverted=True, config=_MOTOR_CFG
    )
    max_vel = config.INTAKE.max_vel
    min_vel = config.INTAKE.min_vel
    desired_power = 0

    def init(self):
        self.left_intake_motor.init()
        self.right_intake_motor.init()

        optimize_normal_talon_no_sensor(self.left_intake_motor)
        optimize_normal_talon_no_sensor(self.right_intake_motor)

    def set_intake_turn_power(self, power: float):
        power = max(min(power, self.max_vel), self.min_vel)
        self.left_intake_motor.set_raw_output(power)
        self.right_intake_motor.set_raw_output(power)

    def get_intake_turn_power(self):
        return (
            self.left_intake_motor.get_sensor_velocity(),
            self.right_intake_motor.get_sensor_velocity(),
        )

    def stop(self):
        self.left_intake_motor.set_raw_output(0)
        self.right_intake_motor.set_raw_output(0)
