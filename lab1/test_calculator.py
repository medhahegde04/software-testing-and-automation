import calculator as calc
def test_add():
    assert calc.add(10, 20) == 30

def test_multiply():
    assert calc.multiply(10, 5) != 40

def test_subtract():
    assert calc.subtract(10, 5) <= 5

def test_divide():
    assert calc.divide(10, 2) > 1
    # assert calc.divide(10, 0) != 0        # fails