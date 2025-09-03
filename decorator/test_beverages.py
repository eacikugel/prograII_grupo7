
import pytest
from beverages import HouseBlend, DarkRoast, Espresso, Decaf
from condiments import Mocha, Whip, Soy, Caramel, Milk
from pretty import pretty_description


def test_simple_espresso():
    b = Espresso()
    assert b.get_description() == "Espresso"
    assert pytest.approx(b.cost(), 0.01) == 1.99


def test_double_mocha():
    b = DarkRoast()
    b = Mocha(b)
    b = Mocha(b)
    assert "Mocha" in b.get_description()
    assert pytest.approx(b.cost(), 0.01) == 1.39


def test_houseblend_soy_size():
    b = HouseBlend()
    b.set_size("VENTI")
    b = Soy(b)
    assert b.get_size() == "VENTI"
    # 0.89 (HouseBlend) + 0.20 (Soy Venti)
    assert pytest.approx(b.cost(), 0.01) == 1.09


def test_caramel_added():
    b = Decaf()
    b = Caramel(b)
    b = Milk(b)
    assert "Leche" in b.get_description()
    # 1.05 + 0.20 + 0.10
    assert pytest.approx(b.cost(), 0.01) == 1.35


def test_pretty_double_mocha():
    b = DarkRoast()
    b = Mocha(b)
    b = Mocha(b)
    b = Whip(b)
    pretty = pretty_description(b)
    assert "Double Mocha" in pretty
    assert "Crema" in pretty
