#!/bin/python3
'''
A python script to control the temperature by sensing temperature and turnning on/off the temperature source.

Input: DHT22 temperature
Output: signal to toggle the power source of the heat source

'''
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
	# main()
	print('main')
