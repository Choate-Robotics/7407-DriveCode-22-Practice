from robotpy_toolkit_7407.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
)

DRIVERCONTROLLER = XBoxController

class Controllers:
    DRIVER = 0
    OPERATOR: int


class Keymap:
    class Drivetrain:
        DRIVE_LEFT = JoystickAxis(Controllers.DRIVER, DRIVERCONTROLLER.L_JOY[1])
        DRIVE_RIGHT = JoystickAxis(Controllers.DRIVER, DRIVERCONTROLLER.R_JOY[1])