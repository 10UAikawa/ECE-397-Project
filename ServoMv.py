#How to code for a Servo in pyfirmata  (Later we will put this is a big while loop)
from pyfirmata import ArduinoMega
from pyfirmata import SERVO
import time


board = ArduinoMega('COM7')  #ArduinoMega connecting to computers COM port

board.digital[6].mode = SERVO   #servo object

#moving servo from 0 to 180 degrees
for i in range(180):
    board.digital[6].write(i)   
    time.sleep(0.01)   #the speed of the servo .01 seconds is a good speed


#moving servo from 180 to 0 degrees
for i in range(180,0,-1):
    board.digital[6].write(i)
    time.sleep(0.01)  #the speed of the servo .01 seconds is a good speed




