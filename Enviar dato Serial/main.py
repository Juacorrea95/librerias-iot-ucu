import pycom

# Disable heartbeat LED
pycom.heartbeat(False)

while True:
    val = input("Ingresar valor: ")
    print('Dato ingresado: ', val)