import random
from time import sleep

import pyautogui


def spam():
    sleep(7)
    count = 0
    while True:
        targetMousePos = [1578, 683]

        currentMousePos = pyautogui.position()

        if (currentMousePos[0] - targetMousePos[0]) ** 2 + (currentMousePos[1] - targetMousePos[1]) ** 2 < 200 ** 2:

            r1 = random.Random().randint(-6, 12)
            r2 = random.Random().randint(-10, 5)
            targetMousePos[0] += r1
            targetMousePos[1] += r2
            pyautogui.moveTo(targetMousePos)
            pyautogui.click()
            sleep(0.01 * abs(r1))
            sleep(0.071)
            count += 1
            delay = 1.5 * 60 + r2
            if count > 100:
                sleep(delay)
                count = 0


if __name__ == '__main__':
    spam()
