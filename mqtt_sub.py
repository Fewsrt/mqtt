import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


# Define Variables
MQTT_HOST = "fasacserver.ddns.net"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "raspi/1"
#
LED1 = 22
LED2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
try:
    def on_connect(self, mosq, obj, rc):
        mqttc.subscribe(MQTT_TOPIC, 0)
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

    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " +
              MQTT_TOPIC + " with QoS: " + str(granted_qos))

    def on_publish(client, userdata, result):  # create function for callback
        print("data published \n")

    # Initiate MQTT Client
    mqttc = mqtt.Client()

    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    mqttc.on_publish = on_publish

    # Connect with MQTT Broker
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Continue monitoring the incoming messages for subscribed topic
    mqttc.loop_forever()

except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    GPIO.cleanup()
# finally:
    # GPIO.cleanup() # this ensures a clean exit
