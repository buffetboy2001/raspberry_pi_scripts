#!/bin/python3
'''
A python script to test the basic behavior of the temperature controller.

'''
import temperature_controller as tc
import time

STARTING_ROOM_TEMPERATURE_C = 19.1  # deg

def main(starting_temp_c:float):
    '''
    Run the test
    '''
    current_room_temp_c = starting_temp_c
    power_pin_state = False

    while True:
        current_room_temp_c = get_temperature_c(current_room_temp_c, power_pin_state)
        print('temp: {}'.format(current_room_temp_c))

        if current_room_temp_c > 24.0 and power_pin_state:
                # power is on and it should be turned off
                power_pin_state = tc.toggle_power(power_pin_state)
        elif current_room_temp_c < 22.0 and not power_pin_state:
                # power is off and it should be turned on
                power_pin_state = tc.toggle_power(power_pin_state)

        time.sleep(tc.SLEEP_DURATION_SECONDS)

    return

def get_temperature_c(current_room_temp_c:float, power_pin_state:bool):
    '''
    Use a simple model to return a temperature.
    '''
    modeled_temperature_rate = 0.01 # deg/sec

    if power_pin_state:
        # the power is on, so increase the room temp
        current_room_temp_c += modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS
    else:
        # the power is off, so decrease the room temp
        current_room_temp_c -= modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS

    return current_room_temp_c

if __name__ == "__main__":
    main(STARTING_ROOM_TEMPERATURE_C)
