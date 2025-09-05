from beverages import Beverage
def pretty_description(beverage):
    """
    Transforma la descripción de una bebida decorada.
    Ejemplo: "Café Dark Roast, Mocha, Mocha, Crema"
    -> "Café Dark Roast, Double Mocha, Crema"
    """
    
    if not isinstance(beverage, Beverage):
        raise TypeError("El argumento 'beverage' debe ser una instancia de Beverage o sus subclases.")
    
    desc = beverage.get_description().split(", ")
    if len(desc) == 1:
        return desc[0]

    base = desc[0] 
    condimentos = desc[1:]

    conteo_condimentos = count_condiments(condimentos)
    return f"{base} con {', '.join(conteo_condimentos)}" 



def count_condiments(condiments):
    counts = {}
    for d in condiments:
        counts[d] = counts.get(d, 0) + 1

    result = []
    for d, c in counts.items():
        if c == 1:
            result.append(d)
        elif c == 2:
            result.append("Double " + d)
        elif c == 3:
            result.append("Triple " + d)
        else:
            result.append(f"{c}x {d}")
    return result