import pigpio
import time

# Initialiser le Pi GPIO
pi = pigpio.pi()

# Le pin GPIO connecté au DHT11 (doit être le même que celui que vous avez configuré)
DHT_PIN = 18

def read_dht11():
    # Démarrer une nouvelle lecture
    pi.set_mode(DHT_PIN, pigpio.OUTPUT)
    pi.write(DHT_PIN, pigpio.LOW)
    time.sleep(0.02)  # 20 ms
    pi.set_pull_up_down(DHT_PIN, pigpio.PUD_OFF)
    pi.set_mode(DHT_PIN, pigpio.INPUT)
    pi.set_watchdog(DHT_PIN, 200)  # Timeout après 200 ms

    # Attendre la réponse du DHT11
    start_time = time.time()
    while pi.read(DHT_PIN) == pigpio.LOW:
        if time.time() - start_time > 0.02:
            return None
    while pi.read(DHT_PIN) == pigpio.HIGH:
        if time.time() - start_time > 0.04:
            return None

    # Lire les données
    data = []
    for i in range(40):
        start_time = time.time()
        while pi.read(DHT_PIN) == pigpio.LOW:
            if time.time() - start_time > 0.04:
                return None
        start_time = time.time()
        while pi.read(DHT_PIN) == pigpio.HIGH:
            if time.time() - start_time > 0.04:
                return None
        data.append(time.time() - start_time)

    # Convertir les temps en bits
    bits = []
    for timing in data:
        bits.append(1 if timing > 0.00005 else 0)

    # Nous devrions maintenant avoir une liste de 40 bits
    # Convertir les bits en octets
    bytes = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte <<= 1
            byte |= bits[i + j]
        bytes.append(byte)

    checksum = bytes[0] + bytes[1] + bytes[2] + bytes[3] & 0xFF
    if bytes[4] == checksum:
        # Les données sont bonnes
        humidity = bytes[0] + bytes[1] / 10
        temperature = bytes[2] + bytes[3] / 10
        return humidity, temperature
    else:
        # Erreur de checksum
        return None

# Lecture des données
humidity, temperature = read_dht11()
if humidity is not None and temperature is not None:
    print(f"Température: {temperature:.1f}°C  Humidité: {humidity:.1f}%")
else:
    print("Échec de la lecture du capteur.")

# Nettoyage des ressources
pi.stop()