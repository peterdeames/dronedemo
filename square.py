'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from tellodji import Tello

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')

def main():
    """ This function will run a test flight to check the drone is connected """
    tello = Tello()
    bat = tello.get_battery()
    logging.info('The battery has %d percent left', bat)
    if bat >= 5:
        tello.takeoff()
        hgt = tello.get_height()
        logging.info('The drone is %dcm in the air', hgt)
        tello.forward(10)
        tello.clockwise(90)
        tello.forward(10)
        tello.clockwise(90)
        tello.forward(10)
        tello.clockwise(90)
        tello.forward(10)
        tello.clockwise(90)
        tello.land()
    else:
        logging.warning('There is not enough power left in the battery \
                        please recharge and try again')
    tello.exit()


if __name__ == "__main__":
    main()
