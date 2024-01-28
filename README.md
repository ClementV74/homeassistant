# Projet Home Assistant Domotique 🚀

Bienvenue dans le projet Home Assistant Domotique ! Ce projet vise à créer un système domotique simple et personnalisable permettant de contrôler l'allumage et l'extinction d'une LED via l'application Home Assistant.

![Home Assistant Image](https://imgs.search.brave.com/zvWJYEk9IHszbYMH8yVnIPs5D-yVerfMoUlpcUYjQfI/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/aG9tZS1hc3Npc3Rh/bnQuaW8vaW1hZ2Vz/L2Jsb2cvMjAyMy0w/OS1oYTEwL2hvbWUt/YXNzaXN0YW50LWxv/Z28tbmV3LnBuZw)

## 📃 Table des Matières 📃

- [Introduction](#introduction)
- [Configuration du Raspberry Pi](#configuration-du-raspberry-pi)
- [Installation du Home Assistant](#installation-du-home-assistant)
- [Configuration du Home Assistant](#configuration-du-home-assistant)
- [Intégration du Capteur de Température DHT11](#intégration-du-capteur-de-température-dht11)
- [Personnalisation](#personnalisation)
- [Ressources Supplémentaires](#ressources-supplémentaires)

## Introduction 👋

Dans ce projet, nous explorons les différentes étapes de la mise en place d'un home assistant personnalisé, offrant une expérience de contrôle de LED à distance. Chaque section du projet est détaillée dans le rapport correspondant, disponible [ici](https://1drv.ms/w/s!AkJOHSOXvqhvl0sIlHi1ev77V9iy?e=ciAqof).

## Configuration du Raspberry Pi ⚙️ 

La première étape consiste à configurer votre Raspberry Pi. Suivez attentivement les instructions détaillées dans la section [Configuration du Raspberry Pi](https://1drv.ms/w/s!AkJOHSOXvqhvl0sIlHi1ev77V9iy?e=ciAqof) du rapport.

## Installation du Home Assistant 🛠️

Une fois votre Raspberry Pi configuré, suivez les étapes d'installation du Home Assistant. Ces étapes sont décrites en détail dans la section [Installation du Home Assistant](https://1drv.ms/w/s!AkJOHSOXvqhvl0sIlHi1ev77V9iy?e=ciAqof) du rapport.

## Configuration du Home Assistant ⚙️

Après l'installation, la configuration du Home Assistant est cruciale. Découvrez comment connecter votre home assistant, installer des addons et personnaliser les fichiers de configuration dans la section [Configuration du Home Assistant](https://1drv.ms/w/s!AkJOHSOXvqhvl0sIlHi1ev77V9iy?e=ciAqof) du rapport.

## Intégration du Capteur de Température DHT11 🌡️

### Ajout du Capteur de Température DHT11

Intégrez un capteur de température DHT11 à votre système domotique. Ce capteur, connecté à un Arduino, transmettra les données de température et d'humidité au Raspberry Pi pour une utilisation dans Home Assistant.

#### Matériel nécessaire

- 1 x Capteur de température DHT11
- 1 x Arduino (Uno, Nano, Mega, etc.)
- Câbles de connexion
- 1 x Résistance de 10k ohms (pour certaines versions du DHT11)

#### Connexion du DHT11 à l'Arduino

1. Connectez la broche VCC du DHT11 au 5V de l'Arduino.
2. Connectez la broche GND du DHT11 au GND de l'Arduino.
3. Connectez la broche de signal du DHT11 à une broche numérique de l'Arduino (par exemple D2).
4. Utilisez une résistance de 10k ohms entre VCC et la broche de signal si nécessaire.

#### Transmission des Données à Raspberry Pi

Connectez l'Arduino au Raspberry Pi via un câble USB. Lisez les données du port série de l'Arduino sur le Raspberry Pi et intégrez-les à Home Assistant.

#### Intégration avec Home Assistant

Configurez votre Raspberry Pi pour lire les données du port série de l'Arduino et utilisez ces données dans Home Assistant pour des automatisations basées sur la température et l'humidité.

## Personnalisation 🎨

Explorez des ajouts, des automatisations et des personnalisations supplémentaires pour faire de ce projet votre propre création. Consultez le rapport pour des suggestions de personnalisation.

## Ressources Supplémentaires 📚

- Rejoignez la communauté Home Assistant sur [Discord](https://discord.com/invite/home-assistant).
- Guide d'installation de Home Assistant : [Raspberry Pi - Home Assistant](https://www.home-assistant.io/installation/raspberrypi).
- Vidéo d'aide : [Lien vers la vidéo](https://www.youtube.com/watch?v=wikJla6AilQ).
- GitHub de Home Assistant : [GitHub](https://github.com/home-assistant)
