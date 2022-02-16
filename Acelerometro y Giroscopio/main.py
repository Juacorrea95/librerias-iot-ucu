import time
import pycom
from pysense import Pysense
from LIS2HH12 import LIS2HH12

py = Pysense()

li = LIS2HH12(py)

# Disable heartbeat LED
pycom.heartbeat(False)

while True:

    pycom.rgbled(0x000060)
    print('\n\n-----------------------------------')
    print('\n\n** 3-Axis Accelerometer (LIS2HH12)')
    print('Acceleration', li.acceleration())
    print('Roll', li.roll())
    print('Pitch', li.pitch())
    pycom.rgbled(0x100000)
    time.sleep(10)
   
