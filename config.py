import ctre

class gearbox():

    class left():

        motorLeft_CAN = ctre.TalonSRX(0)
        motorRight_CAN = ctre.VictorSPX(1)
        motorTop_CAN = ctre.VictorSPX(2)

    class right():

        motorLeft_CAN = ctre.TalonSRX(3)
        motorRight_CAN = ctre.VictorSPX(4)
        motorTop_CAN = ctre.VictorSPX(5)

        



