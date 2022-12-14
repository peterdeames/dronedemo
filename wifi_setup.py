import logging
import sys
import time
from sys import platform
import macwifi

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='[%(levelname)s] - %(message)s')


def connect_tello_mac():
    macwifi.connect("TELLO-AA5203", "")
    time.sleep(5)
    logging.info('Connected to %s', macwifi.get_ssid())


def main():
    try:
        if platform == "darwin":
            # OSX
            connect_tello_mac()
        else:
            logging.error('This script has not been written for %s', platform)
    except Exception as e:
        logging.error('Could not connect to wifi')
        logging.error('%s', e)
        sys.exit(1)


if __name__ == "__main__":
    main()
