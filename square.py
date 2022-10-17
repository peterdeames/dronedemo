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
    try:
        logging.info('Connecting to drone')
        tello.connect()
    except:
        logging.error('Connection failed')
        sys.exit(1)
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
        sleep(1)
        tello.move_forward(50)
        sleep(1)
        tello.rotate_clockwise(90)
        sleep(1)
        tello.move_forward(50)
        sleep(1)
        tello.rotate_clockwise(90)
        sleep(1)
        tello.move_forward(50)
        sleep(1)
        tello.rotate_clockwise(90)
        sleep(1)
        tello.move_forward(50)
        sleep(1)
        tello.rotate_clockwise(90)
        sleep(1)
        tello.move_forward(50)
        sleep(1)
        tello.land()
    else:
        utils.low_bettery()
    tello.end()


if __name__ == "__main__":
    main()
