'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from djitellopy import Tello
import utils
import cv2

# The different levels of logging from the highest to the lowest urgency are:
# CRITICAL | ERROR | WARNING | INFO | DEGUG
logging.basicConfig(stream=sys.stderr, level=logging.INFO,
                    format='[%(levelname)s] - %(message)s')

width = 320
height = 240
startCounter = 1

def main():
    """ This function will run a test flight to check the drone is connected """
    tello = Tello()
    utils.connect()
    if utils.check_battery() >= 5:
        #tello.takeoff()
        tello.streamon()
        hgt = tello.get_height()
        logging.info('The drone is %dcm in the air', hgt)
        #utils.set_height(hgt)
        tello.streamon()
        frame_read = tello.get_frame_read()
        cv2.imwrite("picture.png", frame_read.frame)
        #tello.land()
    else:
        utils.low_battery()
    tello.end()


if __name__ == "__main__":
    main()
