import math
from dataclasses import dataclass
from typing import Union

Number = Union[int, float]

@dataclass
class Point:
    x: Number
    y: Number


class Vector:
    def __init__(self, head: Point, tail: Point=Point(0, 0)) -> None:
        self.head = head
        self.tail = tail


    @property
    def norm(self) -> float:
        dx, dy = self._dxdy()
        return math.sqrt(dx*dx + dy*dy)
    
    @property
    def unit(self) -> 'Vector':
        dx, dy = self._dxdy()
        return Vector(Point(dx/self.norm, dy/self.norm))
    
    def __eq__(self, other: 'Vector') -> bool:
        return self.tail == other.tail and self.head == other.head

    def __add__(self, other) -> 'Vector':
        return Vector(Point(1, 1))
    
    def _dxdy(self):
        return (self.head.x - self.tail.x, self.head.y - self.tail.y)
    