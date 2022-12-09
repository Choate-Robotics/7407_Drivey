import commands2
import ctre
import wpilib
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI

from robot_systems import Robot

from command import drivetrainCustom

from robotpy_toolkit_7407.motors import TalonFX

class Drivey(wpilib.TimedRobot):
    def __init__(self):
        super().__init__(constants.period)

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    # Initialize subsystems
        #commands2.CommandScheduler.getInstance().setPeriod(constants.period)
    # Pneumatics

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    def teleopInit(self):
        #print("Hello")
        commands2.CommandScheduler.getInstance().schedule(drivetrainCustom(Robot.drivetrain))

    def teleopPeriodic(self):
        pass
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Drivey)
