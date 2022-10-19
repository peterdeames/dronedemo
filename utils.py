import logging
import sys
from djitellopy import Tello

tello = Tello()
str1 = 'The battery has'
str2 = 'percent left'

def check_battery():
    bat = tello.get_battery()
    if bat >= 10:
        logging.info('%s %d %s', str1, bat, str2)
    elif bat > 5:
        logging.warn('%s %d %s', str1, bat, str2)
    elif bat <= 5:
        logging.critical('%s %d %s', str1, bat, str2)
    return bat


def low_bettery():
    logging.warning('There is not enough power left in the battery')
    logging.warning('Please recharge and try again')
    sys.exit(1)


def connect():
    try:
        logging.info('Connecting to drone')
        tello.connect()
    except:
        logging.error('Connection failed')
        sys.exit(1)
