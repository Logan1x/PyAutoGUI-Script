PyAutoGUI script to control mouse events
---

PyAutoGUI - PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

For more details : https://github.com/asweigart/pyautogui

To print out 'Live' mouse position coordinates using pyautogui

```python
import pyautogui
pyautogui.displayMousePosition()
```
Here is the video where this is being demonstrated https://youtu.be/dZLyfbSQPXI?t=809



Here is some output :

```BASH
Press Ctrl-C to quit.
X:  0 Y: 1143 RGB: ( 38,  38,  38)
```

To click the left button 
```
pyautogui.click(x=loc, y=loc)
```
