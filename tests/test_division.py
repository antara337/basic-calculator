"""This is the starting test file"""
from app.division import division


def test_division():
    """Divides numbers"""
    assert division(2, 2) == 1
