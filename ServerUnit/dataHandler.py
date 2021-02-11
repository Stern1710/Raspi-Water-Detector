import sys
import paho.mqtt.client as mqtt
import mysql.connector 
from mysql.connector import Error
from gpiozero import LED

MQTT_SERVER = "localhost"
MQTT_WATER = "water"
MQTT_TEMP = "temp"

water = []
temp = []

ledPin = LED("GPIOxy")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_WATER)
    client.subscribe(MQTT_TEMP)

def on_message(client, userdata, msg):
    # 1) Check for message topic and put values into correct list
    if msg.topic == MQTT_WATER:
        water.append(msg.payload)
    if msg.topic == MQTT_TEMP:
        temp.append(msg.payload)

    # 2) If both lists contain elements, pull them from the list and put them into datbase
    # Hint: Make this a while loop with the here displayed conditions
    # Pop date from list, insert into database, then check the loop again if any data is here
    # This most likely only runs for once (bc it checks every time after data is here), but better be sure
    while len(water) > 0 and len(temp) > 0:
        w = water.pop(0)
        t = temp.pop(0)
        try:
            connection = mysql.connector.connect(host='localhost',
                                    database='plantdb',
                                    user='user',
                                    password='password')
            if connection.is_connected():
                cursor = connection.cursor(buffered=True)
                cursor.execute("select database();")
                print w
                if w == "True":
                    print "INSERT INTO datasets (temp, isWatered) VALUES ({0}, b'1');".format(t)
                    cursor.execute("INSERT INTO datasets (temp, isWatered) VALUES ({0}, b'1');".format(t))
					ledPin.off()
                else:
                    print "INSERT INTO datasets (temp, isWatered) VALUES ({0}, b'0');".format(t)
                    cursor.execute("INSERT INTO datasets (temp, isWatered) VALUES ({0}, b'0');".format(t))
					ledPin.on()
                connection.commit()
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
