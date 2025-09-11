from abc import ABC, abstractmethod

# Ingredient products
class Dough:    
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name
class Sauce:    
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name
class Cheese:   
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name
class Clams:    
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name

class Veggies(ABC):
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return self.name

class Onion(Veggies):
    def __init__(self):
        super().__init__("Onion")

class Mushroom(Veggies):
    def __init__(self):
        super().__init__("Mushroom")

class Eggplant(Veggies):
    def __init__(self):
        super().__init__("Eggplant")

class Spinach(Veggies):
    def __init__(self):
        super().__init__("Spinach")

class BlackOlives(Veggies):
    def __init__(self):
        super().__init__("BlackOlives")


class Pepperoni(ABC):
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return self.name

class SlicedPepperoni(Pepperoni):
    def __init__(self):
        super().__init__("Sliced Pepperoni")


# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
    @abstractmethod
    def create_veggies(self) -> list[Veggies]: ...
    @abstractmethod
    def create_pepperoni(self) -> list[Pepperoni, Veggies]: ...
    

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")
    def create_veggies(self) -> list[Veggies]:
        return [Onion(), Mushroom()]
    def create_pepperoni(self) -> list[Pepperoni, Veggies]:
        return list[SlicedPepperoni(), Onion()]

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")
    def create_veggies(self) -> list[Veggies]:
        return [Eggplant(), BlackOlives(), Spinach()]
    def create_pepperoni(self) -> list[Pepperoni, Veggies]:
        return [SlicedPepperoni(), BlackOlives()]
