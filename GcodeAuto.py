import pyautogui, time

time.sleep(2)#give time to close out of program

#stop CNC milling 
def Abort():
    cord = pyautogui.locateCenterOnScreen('Abort.png')
    time.sleep(2)#giving time to find on screen before clicking
    pyautogui.click(cord)

#pause CNC milling
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



    


