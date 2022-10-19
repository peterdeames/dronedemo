'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from djitellopy import Tello
import utils
from time import sleep

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='[%(levelname)s] - %(message)s')

def main():
    """ This function will run a test flight to check the drone is connected """
    tello = Tello()
    utils.connect()
    if utils.check_battery() >= 5:
        tello.takeoff()
        hgt = tello.get_height()
        logging.info('The drone is %dcm in the air', hgt)
        utils.set_height(hgt)
        sleep(1)
        tello.flip_forward()
        sleep(1)
        tello.flip_back()
        sleep(1)
        tello.flip_left()
        sleep(1)
        tello.flip_right()
        sleep(1)
        tello.land()
    else:
        utils.low_battery()
    tello.end()


if __name__ == "__main__":
    main()
