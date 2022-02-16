import pycom

# Disable heartbeat LED
pycom.heartbeat(True)

while True:
    val = input("Ingresar valor: ")
    print('Dato ingresado: ', val)