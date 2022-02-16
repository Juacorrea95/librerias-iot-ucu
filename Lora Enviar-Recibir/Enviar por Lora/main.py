import pycom
from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=915000000, region=LoRa.US915)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    s.send('Ping')
    print("Ping")
    time.sleep(5)
