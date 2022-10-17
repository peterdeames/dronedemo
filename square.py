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
        tello.move_forward(50)
        tello.rotate_clockwise(90)
        tello.move_forward(50)
        tello.rotate_clockwise(90)
        tello.move_forward(50)
        tello.rotate_clockwise(90)
        tello.move_forward(50)
        tello.rotate_clockwise(90)
        tello.move_forward(50)
        tello.land()
    else:
        logging.warning('There is not enough power left in the battery \
                        please recharge and try again')
        sys.exit(1)
    tello.end()


if __name__ == "__main__":
    main()
