from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.current_sum = 0

    def next(self, val: int) -> float:
        self.current_sum += val
        self.queue.append(val)

        if len(self.queue) > self.size:
            front = self.queue.popleft()
            self.current_sum -= front

        return self.current_sum / len(self.queue)
