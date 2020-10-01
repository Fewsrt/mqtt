import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
from subprocess import check_output
from re import findall
import os

# time.sleep(60)
# Define Variables
MQTT_HOST = "192.168.88.220"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "raspi/1"
MQTT_PUB = "relay-1-1-on"
#
LED1 = 16
LED2 = 12
LED3 = 7
LED4 = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
try:
    def on_connect(self, mosq, obj, rc):
        client.subscribe(MQTT_TOPIC, 0)
        client.publish(MQTT_PUB, )
        client.publish("relay-1-off", "OFF")
        client.publish("relay-2-off", "OFF")
        client.publish("relay-3-off", "OFF")
        client.publish("relay-4-off", "OFF")
        client.publish("reboot/status/connect", "System Connected. >.<")
        print("Connect on "+MQTT_HOST)
    # def get_temp():
    #     temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    #     return(findall("\d+\.\d+",temp)[0])

    def on_message(mosq, obj, msg):
        # temp = get_temp
        # client.publish("Home/RPI3/Temp", temp)
        if (msg.payload == 'relay-1-1'):
            client.publish("relay-1-on", "ON")
            GPIO.output(LED1, True)
        if (msg.payload == 'relay-1-0'):
            client.publish("relay-1-off", "OFF")
            GPIO.output(LED1, False)
        if (msg.payload == 'relay-2-1'):
            client.publish("relay-2-on", "ON")
            GPIO.output(LED2, True)
        if (msg.payload == 'relay-2-0'):
            client.publish("relay-2-off", "OFF")
            GPIO.output(LED2, False)
        if (msg.payload == 'relay-3-1'):
            client.publish("relay-3-on", "ON")
            GPIO.output(LED3, True)
        if (msg.payload == 'relay-3-0'):
            client.publish("relay-3-off", "OFF")
            GPIO.output(LED3, False)
        if (msg.payload == 'relay-4-1'):
            client.publish("relay-4-on", "ON")
            GPIO.output(LED4, True)
        if (msg.payload == 'relay-4-0'):
            client.publish("relay-4-off", "OFF")
            GPIO.output(LED4, False)
        if (msg.payload == 'reboot'):
            client.publish("reboot/status/reboot", "System reboot....")
            time.sleep(10)
            print("system reboot")
            # os.system('sudo reboot')
        if (msg.payload == 'shutdown'):
            client.publish("reboot/status/shutdown", "System shutdown....")
            time.sleep(10)
            print("system shutdown")
            # os.system('sudo shutdow -h now')

    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " +
              MQTT_TOPIC + " with QoS: " + str(granted_qos))

    def on_publish(client, userdata, result):  # create function for callback
        print("data published")

    # Initiate MQTT Client
    client = mqtt.Client()

    # Assign event callbacks
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    # Connect with MQTT Broker
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Continue monitoring the incoming messages for subscribed topic
    client.loop_forever()

except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    GPIO.cleanup()
# finally:
    # GPIO.cleanup() # this ensures a clean exit
