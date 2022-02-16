import time
import pycom
from pysense import Pysense
from SI7006A20 import SI7006A20


py = Pysense()
si = SI7006A20(py)

# Disable heartbeat LED
pycom.heartbeat(False)

while True:

    pycom.rgbled(0x000030)
    print('\n\n** Humidity and Temperature Sensor (SI7006A20)')
    print('Humidity', si.humidity())
    print('Temperature', si.temperature())
    pycom.rgbled(0x003000)
    time.sleep(3)

