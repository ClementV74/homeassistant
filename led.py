from gpiozero import LED

# Configuration de la broche GPIO 18 comme sortie
led = LED(18)

try:
    # eteindre la LED en continu
    led.off()

    # Gardez le programme en cours d'exécution
    while True:
        pass

except KeyboardInterrupt:
    # Arrête la boucle lorsque vous appuyez sur Ctrl+C
    led.off()
