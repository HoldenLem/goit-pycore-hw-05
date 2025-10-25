from src.task.task1 import caching_fibonacci


def test_caching_fibonacci_zero():
    fb = caching_fibonacci()
    assert fb(0) == 0

def test_caching_fibonacci_one():
    fb = caching_fibonacci()
    assert fb(1) == 1

def test_caching_fibonacci_valid():
    fb = caching_fibonacci()
    assert fb(10) == 55

def test_cache_caching_fibonacci_valid():
    fb = caching_fibonacci()
    fb(10)
    dictionary = fb.__closure__[0].cell_contents
    assert dictionary[10] == 55

