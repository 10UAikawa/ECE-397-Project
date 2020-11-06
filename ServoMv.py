#How to code for a Servo in pyfirmata  (Later we will put this is a big while loop)
from pyfirmata import ArduinoMega
from pyfirmata import SERVO
import time


board = ArduinoMega('COM7')  #ArduinoMega connecting to computers COM port
pin = 6
range_val_in_degrees = 160
board.digital[pin].mode = SERVO   #servo object

#moving servo from 0 to 160 degrees
for i in range(range_val_in_degrees):
    board.digital[pin].write(i)   
    time.sleep(0.01)   #the speed of the servo .01 seconds is a good speed


#moving servo from 160 to 0 degrees
for i in range(range_val_in_degrees,0,-1):
    board.digital[pin].write(i)
    time.sleep(0.01)  #the speed of the servo .01 seconds is a good speed




