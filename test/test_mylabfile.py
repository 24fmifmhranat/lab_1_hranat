import math


def test_addition():
    """Перевірка додавання двох чисел"""
    assert 3 + 5 == 8
    assert -2 + 7 == 5


def test_factorial():
    """Підрахунок факторіалу"""
    assert math.factorial(5) == 120 
    assert math.factorial(0) == 1


def test_division():
    """Ділення з округленням"""
    result = round(10 / 3, 2) 
    assert result == 3.33


def test_power():
    """Піднесення до степеню"""
    assert pow(2, 3) == 8    
    assert pow(5, 0) == 1
