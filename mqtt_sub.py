import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


# Define Variables
MQTT_HOST = "192.168.88.220"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "raspi/1"
MQTT_PUB = "raspi/2"
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
        client.publish(MQTT_PUB, 0)
        print("Connect on "+MQTT_HOST)

    def on_message(mosq, obj, msg):
        if (msg.payload == 'relay-1-1'):
            GPIO.output(LED1, True)
        if (msg.payload == 'relay-1-0'):
            GPIO.output(LED1, False)
        if (msg.payload == 'relay-2-1'):
            GPIO.output(LED2, True)
        if (msg.payload == 'relay-2-0'):
            GPIO.output(LED2, False)
        if (msg.payload == 'relay-3-1'):
            GPIO.output(LED3, True)
        if (msg.payload == 'relay-3-0'):
            GPIO.output(LED3, False)
        if (msg.payload == 'relay-4-1'):
            GPIO.output(LED4, True)
        if (msg.payload == 'relay-4-0'):
            GPIO.output(LED4, False)

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
