from app.calc import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5

def test_sub():
    assert calc.subtract(5, 2) == 3

def test_mul():
    assert calc.multiply(3, 4) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero_logic():
    try:
        calc.divide(5, 0)
    except TypeError as e:
        assert "Division by zero" in str(e)
