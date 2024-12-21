from handlers.keyboard_handle import NonBlockingKeyboard, BlockingKeyboard
from handlers.mouse_handle import Mouse
from pyautogui import size
from random import randint, uniform, random, shuffle
from time import sleep


class Master():
    def __init__(self, *, keyboard_duration, mouse_duration):
        self.asynkeyboard = NonBlockingKeyboard()
        self.keyboard = BlockingKeyboard(keyboard_duration)
        self.mouse = Mouse(mouse_duration)
        self.width, self.height = size()


    def openInventory(self):
        self.keyboard.pressKey("e")
        iterations = randint(1, 4)
        for i in range(iterations):
            randomSleep = uniform(0.4, 2)
            randomPlace = (randint(0, self.width), randint(0, self.height))
            self.mouse.move(*randomPlace)
            if random() < 0.2: self.mouse.left()
            if random() < 0.2: self.mouse.right()
            sleep(randomSleep)
        self.keyboard.pressKey("esc")
        return iterations


    def jump(self):
        self.keyboard.pressKey("space")


    def lookAround(self):
        self.mouse.move(21, 244)


    def moveAndReturn(self, offset_x, offset_y):
        self.mouse.move(self.width/ 2 + offset_x, self.height/ 2 + offset_y)
        # self.mouse.minecraftMove(offset_x,offset_y)
        sleep(2)
        # self.mouse.move(self.width/ 2, self.height/ 2)
        # sleep(1)
        self.mouse.move(self.width/ 2 , self.height/ 2 )


    def fish(self):
        self.mouse.right()


    def generateKeySequence(self):
        letters = ["w", "a", "s", "d"]
        count = 250
        final_list = letters * count

        shuffle(final_list)
        shuffle(final_list)
        shuffle(final_list)
        shuffle(final_list)
        return final_list


