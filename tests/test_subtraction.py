"""This is the starting test file"""
from app.subtraction import subtraction


def test_subtraction():
    """Subtracts numbers"""
    assert subtraction(2, 2) == 0
