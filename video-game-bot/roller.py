# Author: Ken Zeng 
# Date: 
# This is a bot script that rolls secret shop in Epic Seven for mystic and convenant bookmarks
# Use this script at your own risk

import pyautogui
import time 
import os 

# mac screen size: width=1440, height=90
# TODO: resize images based on screen size

# config parameters: pause adding to account for screen to load
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

# get all relevant target image files 
targets = ['buttons/covenant_bookmark.png',
           'buttons/mystic_bookmark.png']

# find all mystic and convenant bookmarks on the screen 
# TODO: find an image of a mystic bookmark
def find_bookmarks(mode=None):
    """find and purchase all mystic and covenant bookmarks on the screen"""
    for target in targets: 
        for x,y,w,h in pyautogui.locateAllOnScreen(target, confidence=0.99):
            print("book mark found")
            
            # find the buy button closest to the bookmark 
            output = list(pyautogui.locateAllOnScreen("buttons/buy_bookmark.png",confidence=0.99))
            _,idx = min([(abs(loc[1]-y),i) for i,loc in enumerate(output)])
            bx,by,bw,bh = output[idx]
            
            # click the buy button and then confirm
            press_button(x=bx//2+bw//3,y=by//2 + bh//3, mode=mode)
            # pyautogui.moveTo(x=bx//2+bw//3,y=by//2, duration=0.2)
            button_loc = pyautogui.locateCenterOnScreen('buttons/buy.png')
            if button_loc is not None:
                bbx,bby = button_loc
                press_button(x=bbx//2,y=bby//2,mode=mode)
                # pyautogui.moveTo(x=bbx//2, y=bby//2, duration=0.2)
                print("bookmark collected")

def press_button(x,y, mode=None):
    """click the button at pixel location (x,y)"""
    if mode is None:pyautogui.click(x=x,y=y,button='left',clicks=3, interval=0.05)
    # in testing mode, moves mouse to the (x,y) instead of clicking
    else: pyautogui.moveTo(x=x, y=y, duration=0.2)

def scroll_down():
    """scroll to the bottom of the secret shop"""
    # pyautogui.click (startx, starty, clicks=3, interval=0.05)
    pyautogui.scroll(-200)
    # pyautogui.moveTo(startx, starty, duration=0.1)
    # pyautogui.dragTo(startx, starty-200, duration=0.3,button='left')
    
def refresh_shop():
    """click refresh button and confirm refresh"""
    # origianlly confidence is 0.7
    x,y = pyautogui.locateCenterOnScreen('buttons/refresh.png', confidence=0.95)
    pyautogui.click(x=x//2,y=y//2,button='left', clicks=3, interval=0.05) 
    
    # after clicking refresh, press the confirm button
    x,y = pyautogui.locateCenterOnScreen('buttons/confirm.png', confidence=0.95)
    pyautogui.click(x=x//2,y=y//2,button='left', clicks=3, interval=0.05)
    
            
# start this app when you are in the secret shop
if __name__ == "__main__":
    time.sleep(0.5)
    for i in range(10):
        time.sleep(1)
        find_bookmarks() 
        scroll_down()
        find_bookmarks() 
        refresh_shop()
    
