# Time of the day

Implement a 'Time of the day' object with 3 attributes: hour, minute, and seconds.

It should be immutable.

It should support the following behavior:

```python
t1 = Time()

assert str(t1) == '00:00:00'

assert Time(1, 2, 3) == t1.updated(1, 2, 3)

assert Time(0, 1, 2) + Time(1, 0 , 1) == Time(1, 1, 3)
```

Insure that creation, update and addition handles properly `0 <= hour < 24`, `0 <= (minute|second) < 60`.
It's your design decision.

