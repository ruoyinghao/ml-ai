import os
import time
import pyautogui

os.startfile('C:\\Users\\Ruoying\\Desktop\\DS_Project\\excels\\AAPL_2016-04-27_10Q.xlsx')
time.sleep(5)
pyautogui.hotkey('ctrl','pgdn')
time.sleep(1)
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(1)

os.startfile('C:\\Users\\Ruoying\\Desktop\\DS_Project\\excels\\void.png')
time.sleep(3)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyautogui.press('f12')
time.sleep(1)
pyautogui.typewrite('AAPL_2016-04-27_10Q.png')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt','f4')
time.sleep(1)
pyautogui.hotkey('alt','f4')
