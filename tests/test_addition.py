"""This is the starting test file"""
from app.addition import addition


def test_addition():
    """Adds numbers"""
    assert addition(2, 2) == 4 "Addition is not working."
