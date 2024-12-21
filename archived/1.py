import win32gui
import win32api
import win32con
import random as r
import time as t
import asyncio
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

async def sendRightClick(hwnd, x, y):
    clickTime = r.randint(200, 400) / 100
    lParam = y << 16 | x

    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    await asyncio.sleep(clickTime)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, lParam)


async def sendKeyPress(hwnd, key, duration):
    key_mapping = {
        'w': 0x57,
        'a': 0x41,
        's': 0x53,
        'd': 0x44,
    }

    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key_mapping[key], 0)
    await asyncio.sleep(duration)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_mapping[key], 0)


async def keepPressingRightClick(window, getRandomCoordinates, sendRightClick):
    while True:
        x, y = getRandomCoordinates()
        intervalTime = r.uniform(7.8, 11.5)

        print(f"x = {round(x)}    |    y = {round(y)}    |    sleep = {intervalTime}")

        await sendRightClick(window, int(x), int(y))
        await asyncio.sleep(intervalTime)


async def keepMovingAround(window, sendKeyPress):
    keySequence = ['w', 's', 'a', 'd']
    i = 0
    while True:
        intervalTime = r.uniform(5,12.4)
        keystrokeTime = r.randint(200, 400) / 1000
        randomKey = keySequence[i]

        print(f"[{randomKey}]---[{round(keystrokeTime, 2)}ms]")

        await sendKeyPress(window, randomKey, keystrokeTime)
        await asyncio.sleep(intervalTime)

        i = (i + 1) % len(keySequence)

        
async def main(window, sendRightClick, getRandomCoordinates, sendKeyPress):
    await asyncio.create_task(keepMovingAround(window, sendKeyPress))
    await asyncio.create_task(keepPressingRightClick(window, getRandomCoordinates, sendRightClick))



if __name__ == "__main__":
    t.sleep(2)
    try:
        window = findWindow("Minecraft")
        if window is None:
            print("Minecraft window not found")
            exit(1) 
        asyncio.run(main(window, sendRightClick, getRandomCoordinates, sendKeyPress))
    except KeyboardInterrupt:
        print("exiting in 3...")
        t.sleep(1)
        print("exiting in 2...")
        t.sleep(1)
        print("exiting in 1...")
        t.sleep(1)
        exit(0)
