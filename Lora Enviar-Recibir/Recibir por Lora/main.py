from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA,region=LoRa.US915, frequency=915000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print('Start')

while True:
    if s.recv(64) == b'Ping':
        print('Ping Recived')
    time.sleep(5)
