from app.calc import add, sub, mul, divide

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero_logic():
    result = divide(5, 0)
    assert "Error" in result
