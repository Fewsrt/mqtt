import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import time

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.88.220")

while True:
    temp = get_temp()
    serial = getserial()
    publish_message("Home/RPI3/serial", serial)
    publish_message("Home/RPI3/Temp", temp)
    time.sleep(10)