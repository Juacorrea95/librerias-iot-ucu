import socket
import time
import binascii
import struct
import pycom
from network import LoRa

# Disable heartbeat LED
pycom.heartbeat(False)

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region = LoRa.US915)

# create an OTAA authentication parameters
app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('D29CE7DBF25478258A57B91402CC66A6')

print("DevEUI: %s" % (binascii.hexlify(lora.mac())))
print("AppEUI: %s" % (binascii.hexlify(app_eui)))
print("AppKey: %s" % (binascii.hexlify(app_key)))

#Uncomment for US915 / AU915 & Pygate
for i in range(0,8):
    lora.remove_channel(i)
for i in range(16,65):
    lora.remove_channel(i)
for i in range(66,72):
    lora.remove_channel(i)

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0 )

# wait until the module has joined the network
while not lora.has_joined():
    pycom.rgbled(0x140000)
    time.sleep(2.5)
    pycom.rgbled(0x000000)
    time.sleep(1.0)
    print('Not yet joined...')

print('OTAA joined')
pycom.rgbled(0x001400)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)

while True:
    s.setblocking(True)
    pycom.rgbled(0x000014)

    send_data = bytes([255])

    print('Sending data (uplink)...')
    s.send(send_data)
    s.setblocking(False)
    print('Data Sent: ', send_data)
    pycom.rgbled(0x001400)
    time.sleep(10)