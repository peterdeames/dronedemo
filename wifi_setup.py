import logging
import sys
import time
from sys import platform
import macwifi

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')


SSID = 'SKY83C4A'
SSID_PWD = ''


def connect_tello_mac():
    macwifi.connect("TELLO-AA5203", "")
    time.sleep(5)
    logging.info('Connected to %s', macwifi.get_ssid)


def connect_wifi_mac():
    macwifi.connect(SSID, SSID_PWD)
    time.sleep(5)
    logging.info('Connected to %s', macwifi.get_ssid)


def main():
    if platform == "darwin":
        # OSX
        connect_tello_mac()
    else:
        logging.error('This script has not been written for %s', platform)


if __name__ == "__main__":
    main()
