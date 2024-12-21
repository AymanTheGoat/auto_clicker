import pyautogui
import time
import random
import math

class Mouse():
    def __init__(self, duration):
        self.duration = duration

    def move(self ,target_x, target_y, duration=(0.0001, 0.0003), stepsNum=1):
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.0006
        start_x, start_y = pyautogui.position()

        distance = math.sqrt((target_x - start_x) ** 2 + (target_y - start_y) ** 2)

        control_points = [
            (start_x, start_y),
            (start_x + random.uniform(-distance * 0.1, distance * 0.1), start_y + random.uniform(-distance * 0.1, distance * 0.1)),
            (target_x + random.uniform(-distance * 0.05, distance * 0.05), target_y + random.uniform(-distance * 0.05, distance * 0.05)),
            (target_x, target_y),
        ]

        def bezier_curve(t, points):
            """Computes a point on a Bézier curve at time t (0 <= t <= 1)."""
            n = len(points) - 1
            return tuple(
                sum(
                    math.comb(n, i) * (1 - t) ** (n - i) * t ** i * points[i][j] for i in range(n + 1)
                ) for j in range(2)
            )

        steps = int(distance / stepsNum)
        if steps < 10:
            steps = 10

        path = [
            bezier_curve(t / steps, control_points) for t in range(steps + 1)
        ]

        def speed_profile(step, total_steps):
            phase = step / total_steps
            base_speed = (math.sin(phase * math.pi - math.pi / 2) ** 3 + 1) / 2
            return base_speed * random.uniform(0.7, 1.3)

        for i, point in enumerate(path):
            if i > 0:
                prev_point = path[i - 1]
                segment_distance = math.sqrt((point[0] - prev_point[0]) ** 2 + (point[1] - prev_point[1]) ** 2)
                move_duration = segment_distance * speed_profile(i, steps) * random.uniform(*duration)
                time.sleep(move_duration)
            pyautogui.moveTo(point[0], point[1])


    def minecraftMove(self, target_x, target_y, duration=(0.0001, 0.0003), steps_per_unit=0.1, return_to_origin=True, pause_range=(0.2, 0.5)):
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.01

        start_x, start_y = pyautogui.position()

        distance = math.sqrt(target_x ** 2 + target_y ** 2)
        control_points = [
            (start_x, start_y),
            (start_x + random.uniform(-distance * 0.1, distance * 0.1),
            start_y + random.uniform(-distance * 0.1, distance * 0.1)),
            (start_x + target_x + random.uniform(-distance * 0.05, distance * 0.05),
            start_y + target_y + random.uniform(-distance * 0.05, distance * 0.05)),
            (start_x + target_x, start_y + target_y)
        ]

        def bezier_curve(t, points):
            """Computes a point on a Bézier curve at time t (0 <= t <= 1)."""
            n = len(points) - 1
            return tuple(
                sum(
                    math.comb(n, i) * (1 - t) ** (n - i) * t ** i * points[i][j] for i in range(n + 1)
                ) for j in range(2)
            )

        steps = max(int(distance * steps_per_unit), 10)
        path = [bezier_curve(t / steps, control_points) for t in range(steps + 1)]

        def speed_profile(step, total_steps):
            phase = step / total_steps
            base_speed = (math.sin(phase * math.pi - math.pi / 2) ** 3 + 1) / 2
            if step > total_steps * 0.6:  # Slow down in the last 10% of the journey
                base_speed *= 0.5 + (0.5 * (1 - phase))  # Gradual slowdown
            return base_speed * random.uniform(0.7, 1.3)

        for i, point in enumerate(path):
            if i > 0:
                prev_point = path[i - 1]
                segment_distance = math.sqrt((point[0] - prev_point[0]) ** 2 + (point[1] - prev_point[1]) ** 2)
                move_duration = segment_distance * speed_profile(i, steps) * random.uniform(*duration)
                time.sleep(move_duration)
            pyautogui.moveTo(point[0], point[1])

        time.sleep(random.uniform(*pause_range))

        if return_to_origin:
            reverse_target_x = -target_x
            reverse_target_y = -target_y
            self.minecraftMove(reverse_target_x, reverse_target_y, duration, steps_per_unit, return_to_origin=False)


    def right(self):
        randuration = random.uniform(*self.duration)
        pyautogui.rightClick(duration=randuration)


    def left(self):
        randuration = random.uniform(*self.duration)
        pyautogui.leftClick(duration=randuration)

    def getPosition(self):
        return pyautogui.position()
    