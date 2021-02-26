from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import copy
import threading
import sys
import datetime

time.sleep(2)
print("running")
#clean up code by separating it into functions so we can use setters and getters (encapsulate it)
#Use another library or an API call for the topicList instead of the small array
#Verify actions have completed by extracting data from the task manager before proceeding to each step.

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1) #click for 1 s. Too fast and click wont register
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def openChrome():
    pyautogui.press('win')
    print("pressed windows key")
    time.sleep(0.5)
    pyautogui.write('Google Chrome', interval = 0.25)
    print("typing Google Chrome into searchbox")
    time.sleep(0.5)
    pyautogui.press('enter')
    print("hit enter, selected the first item, hopefully Chrome")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 't', interval = 0.5)
    print("opened a new Chrome tab")
    time.sleep(0.5)
    pyautogui.write('gmail.com', interval = 0.25)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4)

def writeRecipients():

    recipientList = ["anonymousvine20@gmail.com", "jasonrobinson625@yahoo.com"]
    
    for index, value in enumerate(recipientList):
        pyautogui.write(value, interval = 0.25)
        time.sleep(0.25)
        pyautogui.press('tab')

username = "usernameText"
password = "passwordText"
subject = "subjectText"
body = "this is a test email"

while keyboard.is_pressed('esc') == False:
    print("In the loop")
    openChrome()

    signInButton = pyautogui.locateCenterOnScreen('signInButton.PNG', confidence = 0.95)
    if signInButton != None:
        click(signInButton.x , signInButton.y )

    signInBoxBlank = pyautogui.locateCenterOnScreen('signInBoxBlank.PNG', confidence = 0.95)
    if signInBoxBlank != None:
        click(signInBoxBlank.x , signInBoxBlank.y )
        pyautogui.write(username, interval = 0.25)
        pyautogui.press('enter')
        
    chooseAccount = pyautogui.locateCenterOnScreen('chooseAccount.PNG', confidence = 0.95)
    if chooseAccount != None:
        click(chooseAccount.x , chooseAccount.y )
    
    cursorAlreadySet = pyautogui.locateCenterOnScreen('cursorAlreadySet.PNG', confidence = 0.95)
    if cursorAlreadySet != None:
        pyautogui.write(password, interval = 0.25)
        pyautogui.press('enter')

    cursorNotSetforPass = pyautogui.locateCenterOnScreen('cursorNotSetforPass.PNG', confidence = 0.95)
    if cursorNotSetforPass != None:
        click(cursorNotSetforPass.x , cursorNotSetforPass.y )

    composeButton = pyautogui.locateCenterOnScreen('composeButton.PNG', confidence = 0.95)
    if composeButton != None:
        click(composeButton.x , composeButton.y )
        time.sleep(2)
        writeRecipients()        
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write(subject, interval = 0.25)
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write(body, interval = 0.25)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'enter', interval = 0.5)
        sys.exit()

sys.exit()

