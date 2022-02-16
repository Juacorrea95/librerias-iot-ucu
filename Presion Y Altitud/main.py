import time
import pycom
from pysense import Pysense
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE

py = Pysense()

# Disable heartbeat LED
pycom.heartbeat(False)

while True:
    pycom.rgbled(0x000030)
    mpPress = MPL3115A2(py,mode=PRESSURE)
    print('\n\n** Barometric Pressure Sensor with Altimeter (MPL3115A2)')
    print('Pressure', mpPress.pressure())
    mpAlt = MPL3115A2(py,mode=ALTITUDE)
    print('Altitude', mpAlt.altitude())
    print('Temperature', mpAlt.temperature())
    pycom.rgbled(0x003000)
    
    time.sleep(10)
