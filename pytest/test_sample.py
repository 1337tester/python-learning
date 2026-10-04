import pytest


testdata = [(1, 0.5, 0.5),
            (5, 6, -1),
            (1, 1, 1)]

def inc(x):
    return x + 1

@pytest.mark.parametrize("a, b, expected", testdata)
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected

def test_answer():
    assert inc(4) == 5

def test_correct():
    assert inc(3) == 4