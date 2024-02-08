import math
from typing import Union

Number = Union[int, float]

class Vector:
    def __init__(self, tail: tuple, head: tuple=(0, 0)) -> None:
        self.head = head
        self.tail = tail

    @property
    def norm(self) -> float:
        dx, dy = self._dxdy()
        return math.sqrt(dx*dx + dy*dy)
    
    @property
    def unit(self) -> 'Vector':
        dx, dy = self._dxdy()
        return Vector((dx/self.norm, dy/self.norm))
    
    def _dxdy(self):
        dx = self.head[0] - self.tail[0]
        dy = self.head[1] - self.tail[1]
        return dx, dy
    