from machine import Pin, PWM
from micropython_servo_pdm import ServoPDM
import time
import sys

# Define the pins for the module
rec = Pin(18, Pin.OUT)  # REC pin connected to GP2
playe = Pin(19, Pin.OUT)  # PLAYE pin connected to GP3
playl = Pin(20, Pin.OUT)  # PLAYL pin connected to GP4
LED = Pin(10, Pin.OUT)
ONLED = Pin(16, Pin.OUT)
Buzzer = Pin(15, Pin.OUT)

ONLED.value(1)

# create a PWM servo controller (21 - pin Pico)
servo_pwm = PWM(Pin(0))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
max_angle = 180
min_angle = 0

# create a servo object
servo = ServoPDM(pwm=servo_pwm, min_us=min_us, max_us=max_us, freq=freq, max_angle=max_angle, min_angle=min_angle,
                 invert=False)


# Play audio continuously
def alert():
    LED.value(1)
    Buzzer.value(1)
    time.sleep(1)
    Buzzer.value(0)
    playe.value(1)  # Start playing
    time.sleep(2)
    playe.value(0)


def mserv():
    # set the 30-degree angle
    servo.set_angle(0)
    time.sleep(5)

    # release the servo
    servo.release()
    time.sleep(2)

    # deinit the servo
    servo.deinit()
    LED.value(0)


while True:
    # read a command from the host
    v = sys.stdin.readline().strip()

    # perform the requested action
    if v.lower() == "on":
        alert()
        mserv()
        print("Done")
