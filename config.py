import ctre

#DRIVETRAIN#
class gearbox:

    class left:

        motorLeft_CAN = ctre.TalonSRX(0)
        motorRight_CAN = ctre.VictorSPX(1)
        motorTop_CAN = ctre.VictorSPX(2)

    class right:

        motorLeft_CAN = ctre.TalonSRX(3)
        motorRight_CAN = ctre.VictorSPX(4)
        motorTop_CAN = ctre.VictorSPX(5)

class sensors:

    class IMU:
        pigeon2 = ctre.Pigeon2(10)

    class encoders:
        left = ctre.CANCoder(9)
        right = ctre.CANCoder(11)

        



