import time
import pycom
from pysense import Pysense
from LTR329ALS01 import LTR329ALS01

py = Pysense()
lt = LTR329ALS01(py)

# Disable heartbeat LED
pycom.heartbeat(False)

while True:

    pycom.rgbled(0x000010)
    print('\n\n** Digital Ambient Light Sensor (LTR-329ALS-01)')
    print('Light', lt.light())
    pycom.rgbled(0x001000)
    time.sleep(3)