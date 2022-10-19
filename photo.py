'''
Run Test flight to check the connection and the battery levels
'''
import logging
import sys
from djitellopy import Tello
import utils
import cv2, math, time

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

        frame_read = tello.get_frame_read()
        myFrame = frame_read.frame
        img = cv2.resize(myFrame, (width, height))
        cv2.imshow("MyResult", img)
        time.sleep(10)

        #tello.land()
    else:
        utils.low_battery()
    tello.end()


if __name__ == "__main__":
    main()
