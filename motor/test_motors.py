from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

motor_hat = Raspi_MotorHAT(addr="put address here")
left_motor = motor_hat.getMotor(1)
right_motor = motor_hat.getMotor(2)

def turn_off_motors():
    left_motor.run(Raspi_MotorHAT.RELEASE)
    right_motor.run(Raspi_MotorHAT.RELEASE)


atexit.register(turn_off_motors)

left_motor.setSpeed(150)
right_motor.setSpeed(150)


left_motor.run(Raspi_MotorHAT.FORWARD)
right_motor.run(Raspi_MotorHAT.FORWARD)

time.sleep(1)