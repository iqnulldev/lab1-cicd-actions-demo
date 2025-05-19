# test_example.py

def add(x, y): # Ця функція НЕ є тестом, бо її назва не починається з test_
    return x + y

def subtract(x, y): # Ця функція НЕ є тестом
    return x - y

def test_add(): # А ось це ТЕСТОВА функція
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract(): # І це ТЕСТОВА функція
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0

# Можна додати ще тестів
def test_always_passes():
    assert True

# Якщо ви додали функцію для множення, тест для неї може виглядати так:
# def multiply(x, y):
#     return x * y
#
# def test_multiply():
#     assert multiply(3, 4) == 12
