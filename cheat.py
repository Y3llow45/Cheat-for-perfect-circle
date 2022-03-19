import pyautogui
import math
import time
import keyboard

R = 200
(x,y) = pyautogui.size()
(X,Y) = pyautogui.position(x/2,y/2)
pyautogui.moveTo(X+R,Y)

while 1:
    if keyboard.is_pressed('q'):
        time.sleep(1)
        pyautogui.moveTo(X+R,Y+42)
        pyautogui.mouseDown(button='right')
        for i in range(364):
            if i%6==0:
                pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+42+R*math.sin(math.radians(i)))
       
        pyautogui.mouseUp(button='right')