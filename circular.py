'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from djitellopy import Tello
import utils

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
        if hgt < 200:
            up = 200 - hgt
            print(up)
            tello.move_up(up)
            hgt = tello.get_height()
            logging.info('The drone is now %dcm in the air', hgt)
        tello.curve_xyz_speed(25, -25, 0, 25, -75, 0, 20)
        tello.land()
    else:
        utils.low_bettery()
    tello.end()


if __name__ == "__main__":
    main()
