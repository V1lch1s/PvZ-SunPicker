#Trabajo basado en el video https://youtu.be/YRAIUA-Oc1Y
#César Antonio Martínez Vilchis.

import pyautogui
import time
import keyboard
import random
import win32api, win32con #pywin32

#Golden Coin RGB: (229, 169,  14)
#Silver Coin RGB: (226, 226, 226)
#Sun Center RGB: (255, 247,   2)

# X axis laptop Display: 1919 || X pc Display: 2559
# Y axis laptop Display: 1079 || Y pc Display: 1439
# El tamaño de la interfaz de PvZ es (799, 599)

#If your device has different dimensions change the values

displayOptionChoice = str(input("Choose if you are using a laptop [L] or desktop [D]: "))

def laptop():
    time.sleep(2)

    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.001) #This pauses the script for 0.001 seconds
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
    while True:
        while keyboard.is_pressed('q') == True:
            pic = pyautogui.screenshot(region=(0,0,1919,1079)) #Because PopCap Interfaces are the Minimizeds, but Maximized on screen beginning at (0,0) Pixel, they extends itselves in relation to your display
            width, height = pic.size
            if pyautogui.locateOnScreen('Sun1.png', confidence = 0.7) != None or pyautogui.locateOnScreen('coin_silver_dollar.png', confidence = 0.7) != None or pyautogui.locateOnScreen('coin_gold_dollar.png', confidence = 0.7): # 0.7 equal to the presition of the image detected
                for x in range(0,width,5):
                    for y in range(0,height,5):
                        r,g,b = pic.getpixel((x, y))
                        if (r in range(201,234) and g in range(226,237) and b in range(80,109)) and (r != 215 and r != 254 and r != 255 and r != 223) and (g != 247 and g != 246 and g != 209 and g != 220) and (b != 131 and b != 110 and b != 111 and b != 106 and b != 84):
                            click(x,y)
                            #pyautogui.moveTo(x,y) #To try the script
                            time.sleep(0.001)
                            break
def desktop():
    time.sleep(2)

    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.001) #This pauses the script for 0.001 seconds
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
    while True:
        while keyboard.is_pressed('q') == True:
            pic = pyautogui.screenshot(region=(0,0,2559,1439)) #Because PopCap Interfaces are pngs Maximized on screen beginning at (0,0) Pixel
            width, height = pic.size
            if pyautogui.locateOnScreen('Sun1.png', confidence = 0.7) != None or pyautogui.locateOnScreen('coin_silver_dollar.png', confidence = 0.7) != None or pyautogui.locateOnScreen('coin_gold_dollar.png', confidence = 0.7): # 0.7 equal to the presition of the image detected
                for x in range(0,width,5):
                    for y in range(0,height,5):
                        r,g,b = pic.getpixel((x, y))
                        # Suns
                        if (r in range(201,234) and g in range(226,237) and b in range(80,109)) and (r != 215 and r != 254 and r != 255 and r != 223) and (g != 247 and g != 246 and g != 209 and g != 220) and (b != 131 and b != 110 and b != 111 and b != 106 and b != 84):
                            click(x,y)
                            #pyautogui.moveTo(x,y) #To try the script
                            time.sleep(0.001)
                        # Silver Coins
                        elif (r == 141 and g == 141 and b == 141): 
                            #click(x,y)
                            pyautogui.moveTo(x,y) #To try the script
                            time.sleep(0.001)
                        # Golden Coins
                        elif (r == 220 and g == 146 and b == 0):
                            #click(x,y)
                            pyautogui.moveTo(x,y) #To try the script
                            time.sleep(0.001)
                            break

if displayOptionChoice.lower() == 'l':
    laptop()
elif displayOptionChoice.lower() == 'd':
    desktop()
    
print("Terminated\nPress Enter...")
input()
