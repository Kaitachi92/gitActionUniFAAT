from app.calc import soma, multiplica, divisao, subtracao, potencia

def test_soma():
    assert soma(2, 3) == 999  # Erro proposital para simular falha no CI

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(3, 2) == 9

def test_subtracao():
    assert subtracao(3, 2) == 1

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divisao():
    assert divisao(6, 2) == 3
