import math

class Vector:
    def __init__(self, tail: tuple, head: tuple=(0, 0)) -> None:
        self.head = head
        self.tail = tail

    @property
    def norm(self) -> float:
        dx = self.head[0] - self.tail[0]
        dy = self.head[1] - self.tail[1]
        return math.sqrt(dx*dx + dy*dy)