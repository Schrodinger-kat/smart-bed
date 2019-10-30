import time
import RPi.GPIO as GPIO

water_sensor = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(water_sensor, GPIO.IN)
x=GPIO.input(water_sensor)
def loop() :
	    x=GPIO.input(water_sensor)
	    if x:
		print("No Liquid  Detected")
		print(x)
	    else:
		print("Liquid Detected")
		print(x)
		return x

