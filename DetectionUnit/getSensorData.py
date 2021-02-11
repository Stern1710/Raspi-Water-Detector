# This program references the mqtt libraries by paho

from sense_hat import SenseHat
from gpiozero import LED
from gpiozero import Button
from time import sleep
import paho.mqtt.publish as publish

# Setup all needed information for MQTT
MQTT_SERVER = "example.org"
MQTT_PATH_WATER = "water"
MQTT_PATH_TEMP = "temp"

# Setup hardare pins and get sensors
enableReading = LED("GPIOxy")
readingPin = Button("GPIOab")
sense = SenseHat()
sense.clear()

#Read temperature and send it over mqtt
temp = round(sense.get_temperature(), 1) - 4
publish.single(MQTT_PATH_TEMP, temp, hostname=MQTT_SERVER)

# Enable the water detection sensor and send data over mqtt
enableReading.on()
sleep(1)
isWatered = readingPin.is_pressed
publish.single(MQTT_PATH_WATER, isWatered, hostname=MQTT_SERVER)
enableReading.off()