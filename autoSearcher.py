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

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1) #click for 1 s. Too fast and click wont register
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

try:
    topicList = ['steak', 'cars', 'food', 'british', 'gift', 'europe', 'life', 'beaches', 'cake recipes']
    
    pyautogui.press('win')
    print("pressed windows key")
    pyautogui.write('Google Chrome')
    print("typing Google Chrome into searchbox")
    pyautogui.press('enter')
    print("hit enter, selected the first item, hopefully Chrome")
    pyautogui.hotkey('ctrl', 't', interval = 0.5)
    print("opened a new Chrome tab")
    randIndex = random.randint(0, len(topicList) - 1)
    pyautogui.write(topicList[randIndex])
    print("searched for", topicList[randIndex])
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
    im1 = pyautogui.screenshot()
    
    now = datetime.datetime.now()
    fileExtension = now.strftime("%Y-%m-%d_%H_%M_%S")
    
    im1.save(str(topicList[randIndex]) + str(fileExtension) + '.png')
    print("saved screenshot")
    
    #pyautogui.moveTo(740, 456)
    #time.sleep(1)
    #pyautogui.moveTo(374, 228)

    #press 'win' key
    #type "Google Chrome" and wait 10 seconds
    #press "enter" and wait 10 seconds
    #press "ctrl+T" to open a new tab
    #search from the topicList array
    

    #waiting = 60 + 240*random.random()
    #topic = random.randint(0,8)
    #print("let us wait", waiting/60, " minutes before searching", topicList[topic])
    #time.sleep(waiting)

    #skipAd = pyautogui.locateCenterOnScreen('adBannerHideout.PNG', confidence = 0.90)
    #if skipAd != None and stage == "initial":
        #click(753, 538)
        #print("skipping an ad")
        #time.sleep(30*random.random())

    #enterSearch = pyautogui.locateCenterOnScreen('hideoutSearchBar.PNG', confidence = 0.95)
    #if enterSearch != None:#trigger a new search, reset the timer
        #click(enterSearch.x, enterSearch.y)
        #pyautogui.write(topicList[topic], interval=0.25)
        #time.sleep(3)
        #press('enter')
        #time.sleep(15)
        #click(406, 303)

        #skipAd2 = pyautogui.locateCenterOnScreen('adBannerHideout.PNG', confidence = 0.90)
        #if skipAd2 != None:
            #click(753, 538)
            #print("skipping an ad")

except KeyboardInterrupt:
    print("pressed a key, now quitting")
    sys.exit()
