#!/bin/python3
'''
A python script to control the temperature by sensing temperature and turnning on/off the 
temperature source. So, this is a simple bang-bang controller.

Input: DHT22 temperature
Output: signal to toggle the power source of the heat source

'''
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

DHT_SENSOR = Adafruit_DHT.DHT22

SLEEP_DURATION_SECONDS = 2.0  # the DHT22 has a hardware frequency of 1Hz. Don't go below that here.
DHT_PIN = 4  # this is the GPIO pin that the DHT22 is connected to. Make sure it represents the physical connection of the sensor.
POWER_PIN = 14 # this is the GPIO pin that is connected to the power source

def toggle_power(power_pin_state:bool):
	'''
	Turn the power on or off (reverse the current state)
	'''
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(POWER_PIN,GPIO.OUT)

	if power_pin_state:
		# It is on, so turn off
		GPIO.output(POWER_PIN,GPIO.LOW)
	else:
		# It is off, so turn on
		GPIO.output(POWER_PIN,GPIO.HIGH)
	
	power_pin_state = not power_pin_state  # reverse state

	return

def main(max_temp_c:float=24.0, min_temp_c:float=22.0, power_pin_state:bool=False):
	'''
	Let's do this.
	'''
	while True:
		humidity_perc, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
		print('temp: {}, humidity: {}'.format(temperature_c, humidity_perc))

		if temperature_c > max_temp_c and power_pin_state:
			# power is on and it should be turned off
			toggle_power(power_pin_state)
		elif temperature_c < min_temp_c and not power_pin_state:
			# power is off and it should be turned on
			toggle_power(power_pin_state)

		time.sleep(SLEEP_DURATION_SECONDS)

	return

if __name__ == "__main__":
	main()
