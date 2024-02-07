import config, constants

from phoenix5 import TalonSRX, ControlMode, FollowerType
from toolkit.subsystem import Subsystem

# Drivetrain subsystem
class Drivetrain(Subsystem):

    # Initialize motors pre-init, DONT MOVE INSIDE INIT OR TESTS CRASH
    left_motor = TalonSRX(config.CAN_IDS_DRIVETRAIN['left_1'])
    right_motor = TalonSRX(config.CAN_IDS_DRIVETRAIN['right_1'])

    left_motor_mirror_1 =  TalonSRX(config.CAN_IDS_DRIVETRAIN['left_2'])
    left_motor_mirror_2 =  TalonSRX(config.CAN_IDS_DRIVETRAIN['left_3'])
    right_motor_mirror_1 = TalonSRX(config.CAN_IDS_DRIVETRAIN['right_2'])
    right_motor_mirror_2 = TalonSRX(config.CAN_IDS_DRIVETRAIN['right_3'])

    # Initialize subclass (from commands2)
    def __init__(self) -> None:
        super().__init__()
    
    # Mirror other left/right motor
    def init(self) -> None:
        self.left_motor_mirror_1.follow(self.left_motor, FollowerType.PercentOutput)
        self.left_motor_mirror_2.follow(self.left_motor, FollowerType.PercentOutput)
        self.right_motor_mirror_1.follow(self.right_motor, FollowerType.PercentOutput)
        self.right_motor_mirror_2.follow(self.right_motor, FollowerType.PercentOutput)

    def set_raw_output(self, speed: float, is_left: bool) -> None: 
        if is_left:
            self.left_motor.set(ControlMode.PercentOutput, speed)
        else:
            self.right_motor.set(ControlMode.PercentOutput, speed)

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        if is_left:
            self.left_motor.set(ControlMode.Velocity, velocity * constants.drivetrain_move_gear_ratio)
        else:
            self.right_motor.set(ControlMode.Velocity, velocity * constants.drivetrain_move_gear_ratio)

    def get_raw_output(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getMotorOutputPercent()
        else:
            return self.right_motor.getMotorOutputPercent()

    def get_velocity(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getSelectedSensorVelocity() / constants.drivetrain_move_gear_ratio
        else:
            return self.right_motor.getSelectedSensorVelocity() /constants.drivetrain_move_gear_ratio
    
    def stop(self) -> None:
        self.left_motor.set(ControlMode.PercentOutput, 0)
        self.right_motor.set(ControlMode.PercentOutput, 0)