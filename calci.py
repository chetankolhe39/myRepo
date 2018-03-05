import pytest

@pytest.fixture()
def addition(z):
    return x + y

@pytest.fixture()
def subtraction(x,y):
    return x - y

@pytest.fixture()
def multiplication(x,y):
    return x * y

@pytest.fixture()
def division(x,y):
    return x / y


@pytest.mark.parametrize("x,y,expected",[
  (2, 4, 6),
  (3, 4, 7),
  (5, 5, 10),
  (6, 10, 16),
  (2, 2, 4),
])
def test_add(x,y,expected,addition):
    assert addition == expected

@pytest.mark.parametrize("x,y,expected",[
   (4, 2, 2),
   (5, 3, 2),
   (8, 5, 3),
   (3, 3, 0),
   (9, 7, 2),
])
def test_sub(x,y,expected,subtraction):
    assert subtraction == expected

@pytest.mark.parametrize("x,y,expected",[
   (2, 4, 8),
   (3, 5, 15),
   (4, 5, 20),
   (3, 3, 9),
   (5, 5, 25),
])
def test_mult(x,y,expected,multiplication):
    assert multiplication == expected

@pytest.mark.parametrize("x,y,expected",[
   (4, 4, 1),
   (30, 5, 6),
   (4, 2, 2),
   (30, 10, 3),
   (66, 11, 6),
])
def test_div(x,y,expected,division):
    assert division == expected

