from robotpy_toolkit_7407.oi import XBoxController


class INTAKE:
    class CAN:
        left_intake_motor: int = 0
        right_intake_motor: int = 1

    max_vel: float = 1
    min_vel: float = -1

    speed_increment: float = 0.1


class CONTROLLERS:
    driver_controller_station_id: int = 0
    operator_controller_station_id: int = 1

    driver_controller_type = XBoxController
    operator_controller_type = XBoxController
