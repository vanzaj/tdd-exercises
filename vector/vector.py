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
    
    def translate(self, dx, dy) -> 'Vector':
        head = Point(self.head.x + dx, self.head.y + dy)
        tail = Point(self.tail.x + dx, self.tail.y + dy)
        return Vector(head, tail)

    def bring_to_origin(self) -> 'Vector':
        return self.translate(-self.tail.x, -self.tail.y)

    def __eq__(self, other: 'Vector') -> bool:
        self0 = self.bring_to_origin()
        other0 = other.bring_to_origin()
        return self0.tail == other0.tail and self0.head == other0.head

    def __add__(self, other: 'Vector') -> 'Vector':
        self0 = self.bring_to_origin()
        other0 = other.bring_to_origin()
        vector_sum = Vector(Point(self0.head.x + other0.head.x, self0.head.y + other0.head.y))
        return vector_sum.translate(self.tail.x, self.tail.y)
    
    def _dxdy(self):
        return (self.head.x - self.tail.x, self.head.y - self.tail.y)

    def __repr__(self):
        return f"Vector({self.head}, {self.tail})"
    