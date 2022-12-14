from robotpy_toolkit_7407.oi import (
    DefaultButton,
    JoystickAxis,
    LogitechController,
    XBoxController,
)

controllerDRIVER = XBoxController


class Controllers:
    DRIVER = 0


class Keymap:
    class Drivetrain:
        LEFT_WHEELS_SPEED = JoystickAxis(Controllers.DRIVER, controllerDRIVER.L_JOY[1])
        RIGHT_WHEELS_SPEED = JoystickAxis(Controllers.DRIVER, controllerDRIVER.R_JOY[1])
        SIDEWAYS = DefaultButton(Controllers.DRIVER, controllerDRIVER.A)
        TANKDRIVE = DefaultButton(Controllers.DRIVER, controllerDRIVER.B)

    class Intake:
        LEFT_DOWN = DefaultButton(Controllers.DRIVER, controllerDRIVER.LB)
        RIGHT_DOWN = DefaultButton(Controllers.DRIVER, controllerDRIVER.RB)
