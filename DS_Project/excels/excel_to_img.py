import os
import time
import pyautogui
from ctypes import windll
import glob
import shutil

fileList=os.listdir(os.curdir)
for eachfile in fileList:
	if eachfile.endswith(".xlsx"):
		ticker,date,tail=eachfile.split("_")

		#open excel
		os.startfile(eachfile)
		time.sleep(3)

		for i in range(1,7):
		#navigate to financial sheet
			pyautogui.hotkey('ctrl','pgdn')
			time.sleep(0.5)
		#select all
			pyautogui.hotkey('ctrl','a')
			time.sleep(0.5)
		#auto fit
			pyautogui.hotkey('alt','h')
			time.sleep(0.5)
			pyautogui.press('o')
			time.sleep(0.5)
			pyautogui.press('i')
			time.sleep(0.5)
		#copy
			pyautogui.hotkey('ctrl','c')
			time.sleep(0.5)
		#open a void.png in mspaint
			os.startfile('void.png')
			time.sleep(1)
		#paste
			pyautogui.hotkey('ctrl','v')
			time.sleep(0.5)
		#save the void.png as new file
			pyautogui.press('f12')
			time.sleep(1)
		#rename
			pyautogui.typewrite(str(i)+'.png')
			time.sleep(0.5)
		#click save
			pyautogui.press('enter')
			time.sleep(0.5)
		#when prompt for data loss, click enter
			pyautogui.press('enter')
			time.sleep(0.5)
		#close new mspaint file
			pyautogui.hotkey('alt','f4')
			time.sleep(0.5)
		#clear keyboard
			if windll.user32.OpenClipboard(None):
				windll.user32.EmptyClipboard()
				windll.user32.CloseClipboard()

		directory=ticker
		if not os.path.exists(directory):
			os.makedirs(directory)
		subdir=ticker+"\\"+date
		if not os.path.exists(subdir):
			os.makedirs(subdir)

		destination = ticker+"\\"+date
		imglist=['1.png','2.png','3.png','4.png','5.png','6.png']
		for imgfile in imglist:
			shutil.copy(imgfile,destination)
			os.remove(imgfile)
		pyautogui.hotkey('alt','f4')
		time.sleep(0.5)
		pyautogui.press('right')
		time.sleep(0.5)
		pyautogui.press('enter')
		time.sleep(0.5)
		os.remove(eachfile)
		
		print(eachfile+" convertion completed and removed")


