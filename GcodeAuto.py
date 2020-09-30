import pyautogui, time
from pyfirmata import ArduinoMega
from pyfirmata import SERVO
import time

time.sleep(2)#give time to close out of program

#Stop CNC milling 
def Abort():
    cord = pyautogui.locateCenterOnScreen('Abort.png')
    time.sleep(2)#giving time to find on screen before clicking
    pyautogui.click(cord)

#Pause CNC milling
def Pause():
    cord = pyautogui.locateCenterOnScreen('Pause.png')
    time.sleep(2)#giving time to find on screen before clicking
    pyautogui.click(cord)

#Reset the CNC
def Reset():
    cord = pyautogui.locateCenterOnScreen('Reset.png')
    time.sleep(2)#giving time to find on screen before clicking
    pyautogui.click(cord)

#Send the CNC file for cutting the PCB
def Send():
    cord = pyautogui.locateCenterOnScreen('Send.png')
    time.sleep(2)#giving time to find on screen before clicking
    pyautogui.click(cord)
    
#Closes the gripper/vaccum
def MvServoClose(ServoNum):
    #moving servo from 0 to 180 degrees
    for i in range(180):
        board.digital[ServoNum].write(i)   
        time.sleep(0.01)   #the speed of the servo .01 seconds is a good speed

#Opens the gripper/vaccum
def MyServoOpen(ServoNum):
    #moving servo from 180 to 0 degrees
    for i in range(180,0,-1):
        board.digital[ServoNum].write(i)
        time.sleep(0.01)  #the speed of the servo .01 seconds is a good speed
    
    

board = ArduinoMega('COM7')  #ArduinoMega connecting to computers COM port
board.digital[6].mode = SERVO   #servo object, (change pin Number depending on which servo)




