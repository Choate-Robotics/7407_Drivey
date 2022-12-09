import commands2
import config
import ctre
from robotpy_toolkit_7407.motors import rev_motors, ctre_motors


class gearbox():

    def __init__(self, leftMotor, rightMotor, topMotor, side) -> None:
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.topMotor = topMotor
        self.side = side
        self.leftMotor.follow(self.topMotor)
        self.rightMotor.follow(self.topMotor)


    def setSpeed(self, percentage):
        self.topMotor.set(ctre.ControlMode.PercentOutput, percentage)


class Drivetrain():

    left = gearbox(
        config.gearbox.left.motorLeft_CAN,
        config.gearbox.left.motorRight_CAN,
        config.gearbox.left.motorTop_CAN,
        "left"
    )

    right = gearbox(
        config.gearbox.right.motorLeft_CAN,
        config.gearbox.right.motorRight_CAN,
        config.gearbox.right.motorTop_CAN,
        "right"
    )
