"""This is the starting test file"""
from app.multiplication import multiplication


def test_multiplication():
    """Multiplies numbers"""
    assert multiplication(2, 2) == 4
