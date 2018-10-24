import pyautogui,time

#pyautogui.displayMousePosition() 

pyautogui.FAILSAFE = True
time.sleep(3)
i=0
while(i<50):
    pyautogui.moveTo(1313,585)
    pyautogui.click(x=1313, y=585)
    i=i+1
    print(i)
