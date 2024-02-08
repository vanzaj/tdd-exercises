# Implement a vector class representing a Euclidean vector in 2D.
# It needs to support the following:
# - [x] Can be instantiated with 1 or 2 (initial/tail, terminal/head) points. If 1 point the other (initial point) defaults to (0,0).
# - [x] Can return vector norm/length/magnitude and unit vector.
# - Can add two vectors
# - Can subtract two vectors
# - Can be multiplied by a scalar
# - Can be compared with another vector
# - Can be dot-multiplied with another vector
import math
from vector import Vector, Number, Point

_P = Point

def almost_equal(a: Number, b: Number) -> bool:
    return abs(a - b) < 1e-6

def test_init_with_tail():
    v = Vector(_P(1, 1))
    assert v.head == _P(1, 1)
    assert v.tail == _P(0, 0)

def test_init_with_head_and_tail():
    v = Vector(head=_P(1, 1), tail=_P(2, 2))
    assert v.head == _P(1, 1)
    assert v.tail == _P(2, 2)


def test_norm():
    assert Vector(_P(3, 4)).norm == 5.0
    assert almost_equal(Vector(_P(1, 1)).norm, math.sqrt(2))


def test_unit_vector():
    u = Vector(_P(1, 1)).unit
    assert almost_equal(u.norm, 1.0)


def test_add_two_vectors_at_origin():
    v1 = Vector(_P(1, 0))
    v2 = Vector(_P(0, 1))
    assert v1 + v2 == Vector(_P(1, 1))
