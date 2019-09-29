import pyautogui,time

a=int(input("Enter your choice : \n 1. Display mouse position \n 2. Click on position \n"))

if(a==1):
    pyautogui.displayMousePosition()

else:
    pyautogui.FAILSAFE = True
    print(" 1. press 1 if you want to input Value  \n 2. press 2 else")
    b = int(input())
    if(b==1):
        print("your choice is 1 so enter value")
        x = int(input("Enter X axis"))
        y = int(input("Enter Y axis"))
        time.sleep(3)
        i=0
        while(i<500):
            pyautogui.click(x, y)
            i=i+1
            print("Clicked " + str(i) + "th times")
    else:        
        i=0
        while(i<500):
            pyautogui.click(x=1271, y=795)
            i=i+1
            print("Clicked " + str(i) + "th times")
