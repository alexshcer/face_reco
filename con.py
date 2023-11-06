import serial
import time

# open a serial connection
s = serial
try:
    s = s.Serial("/dev/ttyACM0", 115200)
except:
  print("Not Connected")

def blink(state):
    if state == 1:
        s.write(b"on\n")
    elif state == 0:
        s.write(b"off\n")

print(s)

"""# blink the led
while True:
    s.write(b"on\n")
    time.sleep(1)
    s.write(b"off\n")
    time.sleep(1)"""
