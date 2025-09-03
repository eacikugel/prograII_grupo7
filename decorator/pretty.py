def pretty_description(beverage):
    """
    Transforma la descripción de una bebida decorada.
    Ejemplo: "Café Dark Roast, Mocha, Mocha, Crema"
    -> "Café Dark Roast, Double Mocha, Crema"
    """
    desc = beverage.get_description().split(", ")
    counts = {}
    for d in desc:
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
    return ", ".join(result)
