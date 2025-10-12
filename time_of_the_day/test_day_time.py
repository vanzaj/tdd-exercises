from day_time import Time


def test_create_time():
    t1 = Time(1, 2, 3)
    assert (t1.hour == 1) and (t1.minute == 2) and (t1.second == 3)
