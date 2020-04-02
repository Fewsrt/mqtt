import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


# Define Variables
MQTT_HOST = "fasacserver.ddns.net"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "raspi/1"
#
LED1 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
try:
  def on_connect(self,mosq, obj, rc):
     mqttc.subscribe(MQTT_TOPIC, 0)
     print("Connect on "+MQTT_HOST)
  def on_message(mosq, obj, msg):
     if (msg.payload=='1'):
           GPIO.output(LED1,True)
           mqttc.publish("relay/on","ON")
           print 'lamp aan'
           print "Topic: " + str(msg.topic)
           print "QoS: " + str(msg.qos)
     if (msg.payload=='0'):
           GPIO.output(LED1,False)
           mqttc.publish("relay/off","OFF")
           print 'lamp uit'
           print "Topic: " + str(msg.topic)
           print "QoS: " + str(msg.qos)

  def on_subscribe(mosq, obj, mid, granted_qos):
          print("Subscribed to Topic: " + 
          MQTT_TOPIC + " with QoS: " + str(granted_qos))

    # Initiate MQTT Client
  mqttc = mqtt.Client()

    # Assign event callbacks
  mqttc.on_message = on_message
  mqttc.on_connect = on_connect
  mqttc.on_subscribe = on_subscribe

    # Connect with MQTT Broker
  mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Continue monitoring the incoming messages for subscribed topic
  mqttc.loop_forever()

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C
    GPIO.cleanup()  
#finally:  
    #GPIO.cleanup() # this ensures a clean exit 