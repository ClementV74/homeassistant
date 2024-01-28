import serial

# Ouvrir la communication série avec le port de l'Arduino
arduino_port = '/dev/ttyUSB0'  # Assurez-vous d'utiliser le bon port
ser = serial.Serial(arduino_port, 9600)  # 9600 est la vitesse (baud rate)

try:
    while True:
        # Lire les données envoyées par l'Arduino
        data = ser.readline().decode('utf-8').strip()
        print(f'Données reçues de l\'Arduino: {data}')
except KeyboardInterrupt:
    ser.close()  # Fermer la communication série en cas d'interruption (Ctrl+C)
