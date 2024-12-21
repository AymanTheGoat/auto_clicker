import win32gui
import win32api
import win32con
from win32api import GetSystemMetrics
import random as r
import time as t



def findWindow(title):
    def callback(hwnd, windows):
        if title.lower() in win32gui.GetWindowText(hwnd).lower():
            windows.append(hwnd)
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None


def getRandomCoordinates():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    
    rectPointX = 15
    rectPointY = 20

    rectX = width / 2 - rectPointX
    rectY = height / 2 - rectPointY

    randXoffset = r.randint(0, rectPointX)
    randYoffset = r.randint(0, rectPointY)

    x = rectX + randXoffset
    y = rectY + randYoffset

    return x, y


def sendRightClick(hwnd, x, y, clickTime):
    
    lParam = y << 16 | x

    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    t.sleep(clickTime)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, lParam)


def keepPressingRightClick(window, getRandomCoordinates, sendRightClick):
    while True:
        x, y = getRandomCoordinates()
        clickTime = 0.1
        # intervalTime = round(r.uniform(7, 11), 2)
        intervalTime = 5

        print(f"x = {round(x)}    |    y = {round(y)}    |    sleep = {intervalTime}")

        sendRightClick(window, int(x), int(y), clickTime)
        t.sleep(intervalTime)


if __name__ == "__main__":
    t.sleep(2)
    try:
        window = findWindow("Minecraft")
        if window is None:
            print("Minecraft window not found")
            exit(1)

        keepPressingRightClick(window, getRandomCoordinates, sendRightClick)

    except KeyboardInterrupt:
        print("exiting in 3...")
        t.sleep(0.4)
        print("exiting in 2...")
        t.sleep(0.3)
        print("exiting in 1...")
        t.sleep(0.3)
        exit(0)