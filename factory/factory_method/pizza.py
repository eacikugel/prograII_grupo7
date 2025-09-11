from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"\nPreparing {self.name}")
        print(f"Adding sauce: {self.sauce}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="NY Style Sauce & Cheese"; self.sauce="Marinara"; self.toppings=["Reggiano cheese"]
 
class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="NY Style Veggie Pizza"; 
        self.sauce="Marinara";
        self.toppings=["Grated Reggiano Cheese", "Mushroom","Onion","Red Pepper"]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="NY Style Pepperoni Pizza"; 
        self.sauce="Marinara";
        self.toppings=["Sliced Pepperoni","Onion","Reaggiano Cheese"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="Chicago Style Deep Dish Cheese"; self.sauce="Plum Tomato Sauce";self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="Chicago Style Veggie Pizza"; 
        self.sauce="Plum Tomato Sauce";
        self.toppings=["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"]
    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        # super().__init__() 
        self.name="Chicago Style Pepperoni Pizza";
        self.sauce="Plum Tomato Sauce"; 
        self.toppings=["Shredded Mozzarella Cheese", "Sliced Pepperoni", "Black Olives"]
    def cut(self): print("Cutting the pizza into square slices")