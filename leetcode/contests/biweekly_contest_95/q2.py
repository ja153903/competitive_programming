from collections import deque


class DataStream:
    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.queue.clear()
        else:
            self.queue.append(num)

        while len(self.queue) > self.k:
            self.queue.popleft()

        return len(self.queue) == self.k
