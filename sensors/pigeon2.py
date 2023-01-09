from config import sensors
import math

class Pigeon2:

    sensors.IMU.pigeon2.configMountPose(0, 0, 0)

    def init():
        sensors.IMU.pigeon2.reset_angle()

    def get_robot_heading():
        return sensors.IMU.pigeon2.getYaw()

    def get_absolute_robot_heading():
        degrees = math.modf(Pigeon2.get_robot_heading() / 360)
        return 360 * -degrees[0]


    # reset the gyro
    def reset_angle():
        sensors.IMU.pigeon2.setYaw(0)