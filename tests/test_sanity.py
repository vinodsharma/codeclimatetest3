import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from src.dummy import dummy_func
except ImportError:
    raise Exception("src.dummy Import Error")


def test_sanity():
    assert True is True


def test_sanity2():
    assert True is True


def test_dummy_func():
    eo = 1

    o = dummy_func(True)

    assert eo == o
