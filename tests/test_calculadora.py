import pytest
from src.calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_adicao(calc):
    assert calc.adicao(2, 3) == 5
    assert calc.adicao(-1, -1) == -2
    assert calc.adicao(-1, 1) == 0

def test_subtracao(calc):
    assert calc.subtracao(5, 3) == 2
    assert calc.subtracao(0, 1) == -1
    assert calc.subtracao(-3, -7) == 4

def test_multiplicacao(calc):
    assert calc.multiplicacao(3, 4) == 12
    assert calc.multiplicacao(-2, 3) == -6
    assert calc.multiplicacao(0, 10) == 0

def test_divisao(calc):
    assert calc.divisao(10, 2) == 5
    assert calc.divisao(-6, 3) == -2
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        calc.divisao(5, 0)

def test_fatorial(calc):
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    with pytest.raises(ValueError, match="Fatorial de número negativo não é permitido."):
        calc.fatorial(-3)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(2, -2) == 0.25
