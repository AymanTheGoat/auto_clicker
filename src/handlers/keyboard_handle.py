import pyautogui
import random
from threading import Timer
import threading
import time 


class NonBlockingKeyboard():
    def __init__(self):
        self.active_timers = {}

    def pressKey(self, key):
        if duration is None:
            duration = random.uniform(0.1, 0.5)
        
        pyautogui.keyDown(key)
        
        timer = Timer(duration, self._release_key, args=[key])
        timer.start()
        
        self.active_timers[key] = timer

    def _release_key(self, key):
        pyautogui.keyUp(key)
        if key in self.active_timers:
            del self.active_timers[key]

    def cancelKey(self, key):
        if key in self.active_timers:
            self.active_timers[key].cancel()
            del self.active_timers[key]
            pyautogui.keyUp(key)

    def pressKeys(self, keys, durations=None):
        if durations is None:
            durations = [random.uniform(0.1, 0.5) for _ in keys]
        
        for key, duration in zip(keys, durations):
            self.pressKey(key, duration)


class BlockingKeyboard():
    def __init__(self, duration=None):
        self.duration = duration

    def pressKey(self, key, duration=None):
        if duration is None:
            duration = random.uniform(*self.duration)

        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)
        
        return duration

    def pressKeys(self, keys, durations=None):
        if durations is None:
            durations = [random.uniform(*self.duration) for _ in keys]

        threads = []

        for key, duration in zip(keys, durations):
            thread = threading.Thread(target=self.pressKey, args=(key, duration))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


