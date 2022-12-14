import logging
import sys
from djitellopy import Tello

tello = Tello()
flight_height = 150
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


def low_battery():
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

def set_height(hgt):
    if hgt < flight_height:
        up = flight_height - hgt
        tello.move_up(up)
        hgt = tello.get_height()
        logging.info('The drone is now %dcm in the air', hgt)
