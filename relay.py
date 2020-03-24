import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

GPIO.setup(23, GPIO.OUT) # GPIO Assign mode
GPIO.output(23, GPIO.LOW) # out
GPIO.output(23, GPIO.HIGH) # on