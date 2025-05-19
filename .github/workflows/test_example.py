# test_example.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0

# Приклад тесту, який може впасти, якщо логіка неправильна
# def test_multiply_by_two():
#     assert add(2, 2) == 4 # Це правильно
#     # assert add(3, 3) == 5 # Цей тест впаде, бо 3+3=6, а не 5