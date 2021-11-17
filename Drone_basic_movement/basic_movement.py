import cv2
from djitellopy import tello
import time


drone = tello.Tello()
drone.connect()
print(drone.get_battery())

#cho may bay cat canh
drone.takeoff()
drone.send_rc_control(0,50,0,0) #di chuyen ve phia truoc 50cm
time.sleep(3)