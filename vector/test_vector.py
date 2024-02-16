# Implement a vector class representing a Euclidean vector in 2D.
# It needs to support the following:
# - [x] Can be instantiated with 1 or 2 (initial/tail, terminal/head) points. If 1 point the other (initial point) defaults to (0,0).
# - [x] Can return vector norm/length/magnitude and unit vector.
# - [x] Can add two vectors
# - [x] Can be compared with another vector
# - Can be multiplied by a scalar
# - Can subtract two vectors
# - Can be dot-multiplied with another vector

import math
from vector import Vector, Number, Point

P_ = Point


def almost_equal(a: Number, b: Number) -> bool:
    return abs(a - b) < 1e-6


def test_init_with_head_only():
    v = Vector(P_(1, 1))
    assert v.head == P_(1, 1)
    assert v.tail == P_(0, 0)


def test_init_with_head_and_tail():
    v = Vector(head=P_(1, 1), tail=P_(2, 2))
    assert v.head == P_(1, 1)
    assert v.tail == P_(2, 2)


def test_norm():
    assert Vector(P_(3, 4)).norm == 5.0
    assert almost_equal(Vector(P_(1, 1)).norm, math.sqrt(2))


def test_unit_vector():
    u = Vector(P_(1, 1)).unit
    assert almost_equal(u.norm, 1.0)


def test_add_two_vectors_at_origin():
    v1 = Vector(P_(1, 0))
    v2 = Vector(P_(0, 1))
    assert v1 + v2 == Vector(P_(1, 1))


def test_translate_vector():
    v = Vector(P_(1, 1)).translate(1, 0)
    assert v.tail == P_(1, 0)
    assert v.head == P_(2, 1)


def test_add_two_vectors_not_at_origin():
    v1 = Vector(P_(2, 0), P_(1, 0))
    v2 = Vector(P_(0, 1))
    assert v1 + v2 == Vector(P_(2, 1), P_(1, 0))


def test_equal_vectors():
    v = Vector(P_(1, 1))
    vv = v.translate(1, 0)
    assert v == Vector(P_(1, 1))
    assert vv == Vector(P_(1, 1))
