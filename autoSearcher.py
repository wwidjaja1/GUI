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

try:
    topicList = ['steak', 'cars', 'food', 'british', 'gift', 'europe', 'life', 'beaches', 'cake recipes']
    
    pyautogui.press('win')
    print("pressed windows key")
    time.sleep(3)
    pyautogui.write('Google Chrome', interval = 0.25)
    print("typing Google Chrome into searchbox")
    time.sleep(3)
    pyautogui.press('enter')
    print("hit enter, selected the first item, hopefully Chrome")
    time.sleep(3)
    pyautogui.hotkey('ctrl', 't', interval = 0.5)
    print("opened a new Chrome tab")
    time.sleep(3)
    randIndex = random.randint(0, len(topicList) - 1)
    pyautogui.write(topicList[randIndex], interval = 0.25)
    print("searched for", topicList[randIndex])
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
    im1 = pyautogui.screenshot()
    
    now = datetime.datetime.now()
    fileExtension = now.strftime("%Y-%m-%d_%H_%M_%S")
    
    im1.save(str(topicList[randIndex]) + str(fileExtension) + '.png')
    print("saved screenshot")
    

except KeyboardInterrupt:
    print("pressed a key, now quitting")
    sys.exit()
