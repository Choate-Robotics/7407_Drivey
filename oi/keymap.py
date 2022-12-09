from robotpy_toolkit_7407.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
)

controllerDRIVER = XBoxController

class Controllers:
    DRIVER = 0
    OPERATOR = 1


class Keymap:
    
    class Drivetrain:

        LEFT_AXIS_Y = JoystickAxis(Controllers.DRIVER, controllerDRIVER.L_JOY[1])
        LEFT_AXIS_X = JoystickAxis(Controllers.DRIVER, controllerDRIVER.L_JOY[0])
        RIGHT_AXIS_Y = JoystickAxis(Controllers.DRIVER, controllerDRIVER.R_JOY[1])
        RIGHT_AXIS_X = JoystickAxis(Controllers.DRIVER, controllerDRIVER.R_JOY[0])

        DRIVE_STYLE = DefaultButton(Controllers.DRIVER, controllerDRIVER.SELECT)
