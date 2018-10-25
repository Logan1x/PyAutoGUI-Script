import pyautogui,time

a=int(input("Enter your choice : \n 1. Display mouse position \n 2. Click on position \n"))

if(a==1):
    pyautogui.displayMousePosition() 

else:
    pyautogui.FAILSAFE = True
    time.sleep(3)
    i=0
    while(i<500):
        pyautogui.click(x=1310, y=566)
        i=i+1
        print("Clicked " + str(i) + "th times")
