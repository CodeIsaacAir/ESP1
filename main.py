from mq135 import MQ135
from MQ7 import MQ7
from dc_motor import DCMotor
from led_control import LED
#from communication_1 import ESP32_COM
import machine
from machine import Pin, PWM 
import network
from machine import UART
import time
import struct




mq135=MQ135(machine.Pin(15))
mq7=MQ7(machine.Pin(12))
while True:
    co2=mq135.get_ppm()
    co=mq7.readCarbonMonoxide()
    print("co2:",co2)
    print("co:",co)
    
