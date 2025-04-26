import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected



@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (4, 5, 20),
    (0, 5, 0),
    (-3, 3, -9),
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (-9, 3, -3),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),
    (10, -1, 0.1)
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6)
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (7, 13)
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected


def test_precise_add(precise_calculator):
    assert precise_calculator.add(1.111, 2.222) == 3.33
