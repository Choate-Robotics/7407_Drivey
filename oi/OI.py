from robotpy_toolkit_7407.utils import logger
import constants
from oi.keymap import Keymap
logger.info("Hi, I'm OI!")


class OI:
    @staticmethod
    def init() -> None:
        logger.info("Initializing OI...")

    @staticmethod
    def map_controls():
        logger.info("Mapping controls...")
        pass

    def driveStyle():
        if constants.driveType == "arcade":
            constants.driveType = "tank"
            return
        if constants.driveType == "tank":
            constants.driveType = "diff"
            return
        if constants.driveType == "diff":
            constants.driveType = "arcade"
            return
        print(constants.driveType)

    Keymap.Drivetrain.DRIVE_STYLE().whenPressed(driveStyle)
