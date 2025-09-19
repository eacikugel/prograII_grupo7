# Ejemplo de esqueleto de prueba con pytest
from .store import NYPizzaStore, ChicagoPizzaStore
from .ingredients import Dough, Clams

def test_ny_style_pizza():
    store = NYPizzaStore()

    pizza = store.order_pizza("pepperoni")

    assert "NY Style" in pizza.name

def test_chicago_style_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("cheese")
    assert "Chicago Style" in pizza.name


def test_ny_cheese_pizza_has_correct_dough():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza.dough, Dough)
    assert str(pizza.dough) == "Thin Crust Dough"

def test_chicago_clam_pizza_has_correct_clams():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert isinstance(pizza.clam, Clams)
    assert str(pizza.clam) == "Frozen Clams"

def test_ny_clam_pizza_has_correct_clams():
    store = NYPizzaStore()
    pizza = store.order_pizza("clam")
    assert isinstance(pizza.clam, Clams)
    assert str(pizza.clam) == "Fresh Clams"