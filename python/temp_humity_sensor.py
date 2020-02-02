#!/bin/python3
'''
A script to pull data from the DHT22 temperature & humidity sensor.
'''

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # this is the GPIO pin. Make sure it represents the physical connection of the sensor

while True:
	humidity_perc, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	print('temp: {}, humidity: {}'.format(temperature_c, humidity_perc))
	time.sleep(1.0)

