import logging
import sys
from djitellopy import Tello

tello = Tello()

def check_battery():
    bat = tello.get_battery()
    if bat >= 10:
        logging.info('The battery has %d percent left', bat)
    elif bat > 5:
        logging.warn('The battery has %d percent left', bat)
    elif bat <= 5:
        logging.critical('The battery has %d percent left', bat)
    return bat