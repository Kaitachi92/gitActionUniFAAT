from app.calc import soma, multiplica, divisao, subtracao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(3, 2) == 1

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divisao():
    assert divisao(6, 2) == 3
