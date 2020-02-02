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

    while True:
        current_room_temp_c = get_temperature_c(current_room_temp_c)
        print('temp: {}'.format(current_room_temp_c))

        if current_room_temp_c > 24.0 and tc.POWER_PIN_STATE:
                # power is on and it should be turned off
                tc.toggle_power()
        elif current_room_temp_c < 22.0 and not tc.POWER_PIN_STATE:
                # power is off and it should be turned on
                tc.toggle_power()

        time.sleep(tc.SLEEP_DURATION_SECONDS)

    return

def get_temperature_c(current_room_temp_c:float):
    '''
    Use a simple model to return a temperature.
    '''
    modeled_temperature_rate = 0.01 # deg/sec

    if tc.POWER_PIN_STATE:
        # the power is on, so increase the room temp
        current_room_temp_c += modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS
    else:
        # the power is off, so decrease the room temp
        current_room_temp_c -= modeled_temperature_rate*tc.SLEEP_DURATION_SECONDS

    return current_room_temp_c

if __name__ == "__main__":
    tc.POWER_PIN_STATE = False
    print(tc.POWER_PIN_STATE)    
    main(STARTING_ROOM_TEMPERATURE_C)
