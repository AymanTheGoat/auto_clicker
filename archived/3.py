import win32gui
import win32api
import win32con
import random as r
import time as t
import threading
from win32api import GetSystemMetrics


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


# def fakeFocusWindow(hwnd):
#     style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
#     new_style = style | win32con.WS_VISIBLE
#     win32gui.SendMessage(hwnd, win32con.WM_SETFOCUS, 0, 0)
#     win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)


def sendRightClick(hwnd, x, y, clickTime):
    
    lParam = y << 16 | x

    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    t.sleep(clickTime)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, lParam)


def sendKeyPress(hwnd, key, duration):
    key_mapping = {
        'w': 0x57,
        'a': 0x41,
        's': 0x53,
        'd': 0x44,
    }

    press_time = t.time()
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key_mapping[key], 0)
    print(f"Key DOWN [{key}] at {press_time}")

    t.sleep(duration)

    release_time = t.time()
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key_mapping[key], 0)
    print(f"Key UP [{key}] at {release_time}")


def keepPressingRightClick(window, getRandomCoordinates, sendRightClick):
    while True:
        x, y = getRandomCoordinates()
        clickTime = 0.1
        # intervalTime = round(r.uniform(7, 11), 2)
        intervalTime = 5

        print(f"x = {round(x)}    |    y = {round(y)}    |    sleep = {intervalTime}")

        sendRightClick(window, int(x), int(y), clickTime)
        t.sleep(intervalTime)


def keepMovingAround(window, sendKeyPress):
    keySequence = ['w', 's', 'a', 'd']
    i = 0
    while True:
        # intervalTime = r.uniform(5,12.4)
        # keystrokeTime = r.randint(200, 400) / 1000
        keystrokeTime = 0.1
        intervalTime = 5

        randomKey = keySequence[i]
        # randomKey2 = keySequence[i+1]

        print(f"[{randomKey}]---[{round(keystrokeTime, 2)}ms]")

        sendKeyPress(window, randomKey, keystrokeTime)
        # sendKeyPress(window, randomKey2, keystrokeTime)
        
        t.sleep(intervalTime)

        i = (i + 1) % len(keySequence)


if __name__ == "__main__":
    t.sleep(2)
    try:
        window = findWindow("Minecraft")
        if window is None:
            print("Minecraft window not found")
            exit(1)

        thread = threading.Thread(target=keepPressingRightClick, args=(window, getRandomCoordinates, sendRightClick))
        thread.daemon = True
        thread.start()

        keepMovingAround(window, sendKeyPress)

    except KeyboardInterrupt:
        print("exiting in 3...")
        t.sleep(0.4)
        print("exiting in 2...")
        t.sleep(0.3)
        print("exiting in 1...")
        t.sleep(0.3)
        exit(0)
