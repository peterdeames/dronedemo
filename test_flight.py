'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from djitellopy import Tello
import wifi_setup

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')

def main():
    """ This function will run a test flight to check the drone is connected """
    tello = Tello()
    try:
        logging.info('Connecting to drone')
        tello.connect()
    except:
        logging.error('Connection failed')
        wifi_setup.connect_wifi_mac()
        sys.exit(1)
    bat = tello.get_battery()
    logging.info('The battery has %d percent left', bat)
    if bat >= 10:
        tello.takeoff()
        hgt = tello.get_height()
        logging.info('The drone is %dcm in the air', hgt)
        tello.land()
    else:
        logging.warning('There is not enough power left in the battery \
                        please recharge and try again')
    wifi_setup.connect_wifi_mac()


if __name__ == "__main__":
    main()
