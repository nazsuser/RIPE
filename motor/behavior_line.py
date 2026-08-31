from model import robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep

r = robot.RIPE()
r.set_left(80)
r.set_right(80)
sleep(5)