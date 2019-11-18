import pyautogui

def draw(x):
    xd = 800
    yd = 240
    pyautogui.mouseDown()
    while True:
        pyautogui.moveTo(xd, yd)
        pyautogui.moveRel(x, 0)
        pyautogui.moveRel(0, -x)
        pyautogui.moveRel(-x, 0)
        pyautogui.moveRel(0,x)
        pyautogui.moveRel((x * 4), 0)
        pyautogui.moveRel(0, x)
        pyautogui.moveRel(-(x * 4), 0)
        pyautogui.moveRel(0, x)
        pyautogui.moveRel(x, 0)
        pyautogui.moveRel(0, -(x * 3))
        pyautogui.moveRel(-x, 0)
        pyautogui.moveRel(0, x)

        pyautogui.moveRel(0 , x*7)
        pyautogui.moveTo(xd, yd + (x*7))

        pyautogui.moveRel(x, 0)
        pyautogui.moveRel(0, -x * 3)
        pyautogui.moveRel(-x, 0)
        pyautogui.moveRel(0, x)
        pyautogui.moveRel(x * 4, 0)
        pyautogui.moveRel(0, x)
        pyautogui.moveRel(-x * 4, 0)
        
        
        pyautogui.moveRel(0, -x * 6)

        

