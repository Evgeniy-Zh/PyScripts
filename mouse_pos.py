import pyautogui

if __name__ == '__main__':
    posX: int = 0
    posY: int = 0

    while (True):
        currentMouseX, currentMouseY = pyautogui.position()  # Returns two integers, the x and y of the mouse cursor's current position.
        if posX != currentMouseX and posY != currentMouseY:
            print(currentMouseX, currentMouseY)
            posX, posY = currentMouseX, currentMouseY
