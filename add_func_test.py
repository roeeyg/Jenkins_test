# test_add_func.py

import add_func


def test_add():
    assert add_func.add(1, 2) == 3
    assert add_func.add(0, 0) == 0
    assert add_func.add(-1, 1) == 0
    assert add_func.add(2.5, 3.5) == 6.0
