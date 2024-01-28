"""This is the starting test file"""

from app.division import division


def test_zero_division():
    """Divides by 0"""
    assert division(2, 0) == ZeroDivisionError
