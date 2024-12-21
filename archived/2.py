import ctypes
import time

# Define constants
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

def send_mouse_event(dx, dy):
    input_struct = INPUT(type=INPUT_MOUSE,
                         mi=MOUSEINPUT(dx=dx, dy=dy, mouseData=0, dwFlags=MOUSEEVENTF_MOVE, time=0, dwExtraInfo=None))
    ctypes.windll.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(input_struct))

def move_mouse_smoothly(dx, dy, duration=1.0):
    steps = 100
    step_dx = dx / steps
    step_dy = dy / steps

    for i in range(steps):
        send_mouse_event(int(step_dx), int(step_dy))
        time.sleep(duration / steps)

# Main test
if __name__ == "__main__":
    time.sleep(2)
    # Example: Rotate Minecraft view by moving mouse right
    move_mouse_smoothly(2000, 0, duration=1.0)