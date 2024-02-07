# Implement a vector class representing a Euclidean vector in 2D.
# It needs to support the following:
# - [x] Can be instantiated with 1 or 2 (initial/tail, terminal/head) points. If 1 point the other (initial point) defaults to (0,0).
# - Can return vector norm/length/magnitude and unit vector.
# - Can add two vectors
# - Can subtract two vectors
# - Can be multiplied by a scalar
# - Can be compared with another vector
# - Can be dot-multiplied with another vector
from vector import Vector

def test_init_with_tail():
    v = Vector((1, 1))
    assert v.head == (0, 0)
    assert v.tail == (1, 1)

def test_init_with_head_and_tail():
    v = Vector(head=(1, 1), tail=(2, 2))
    assert v.head == (1, 1)
    assert v.tail == (2, 2)
