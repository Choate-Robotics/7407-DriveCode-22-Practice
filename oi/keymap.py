from robotpy_toolkit_7407.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
)

DriverCONTROLLER = XBoxController


class Controllers:
    DRIVER = 0
    OPERATOR: int


class Keymap:
    class Drivetrain:
        left_joy = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.L_JOY[1])
        right_joy = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.R_JOY[1])
