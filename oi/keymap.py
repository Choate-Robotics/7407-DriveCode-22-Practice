from robotpy_toolkit_7407.oi import DefaultButton

from config import CONTROLLERS

controllerDRIVER = CONTROLLERS.driver_controller_type
controllerOPERATOR = CONTROLLERS.operator_controller_type


class Keymap:
    class Intake:
        DECREASE_SPEED: DefaultButton(
            CONTROLLERS.driver_controller_station_id, controllerDRIVER.LT
        )
        INCREASE_SPEED: DefaultButton(
            CONTROLLERS.operator_controller_station_id, controllerDRIVER.RT
        )
        STOP_MOTORS: DefaultButton(
            CONTROLLERS.driver_controller_station_id, controllerDRIVER.A
        )
