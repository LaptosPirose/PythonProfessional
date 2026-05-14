import pytest
from src.calculadora import Calculadora


@pytest.fixture(name="calc_test")
def calc():
    return Calculadora()


def test_soma(calc_test: Calculadora):
    assert calc_test.soma(2, 3) == 5


def test_soma_negativo(calc_test: Calculadora):
    assert calc_test.soma(-1, -1) == -2
