#!/bin/python3
'''
A python script to test the basic behavior of the temperature controller.

'''
import temperature_controller as tc
import time

STARTING_ROOM_TEMPERATURE_C = 19.1  # deg
CURRENT_ROOM_TEMPERATURE_C = None

def get_temperature_c():
    '''
    Use a simple model to return a temperature.
    '''
    modeled_temperature_rate = 0.01 # deg/sec

    if tc.POWER_PIN_STATE:
        # the power is on, so increase the room temp
        CURRENT_ROOM_TEMPERATURE_C = CURRENT_ROOM_TEMPERATURE_C + modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS
    else:
        # the power is off, so decrease the room temp
        CURRENT_ROOM_TEMPERATURE_C = CURRENT_ROOM_TEMPERATURE_C - modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS

    return

def main():
    '''
    Run the test
    '''
    CURRENT_ROOM_TEMPERATURE_C = STARTING_ROOM_TEMPERATURE_C

    while True:
        get_temperature_c()
        print('temp: {}'.format(CURRENT_ROOM_TEMPERATURE_C))

		if CURRENT_ROOM_TEMPERATURE_C > 24.0 and tc.POWER_PIN_STATE:
			# power is on and it should be turned off
			toggle_power()
		elif CURRENT_ROOM_TEMPERATURE_C < 22.0 and not tc.POWER_PIN_STATE:
			# power is off and it should be turned on
			toggle_power()

		time.sleep(tc.SLEEP_DURATION_SECONDS)

    return

if __name__ == "__main__":
	main()