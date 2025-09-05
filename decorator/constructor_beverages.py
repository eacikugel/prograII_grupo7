from abc import abstractmethod


def build_beverage(base, size=None, condiments=None):
    
    """
    Construye una bebida con condimentos.
    base: clase base de la bebida (Espresso, DarkRoast, etc.)
    size: tamaño (TALL, GRANDE, VENTI)
    condimentos: lista de clases decoradoras [Soy, Mocha, Whip]
    """
    if size:
        beverage = base(size)
    else:
        beverage = base()

    if condiments:
        for condiment_cls in condiments:
            beverage = condiment_cls(beverage)

    return beverage


