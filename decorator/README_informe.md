
## Para propagar size:
- Definimos el atributo size en la clase abstracta Beverage con valor por defecto "VENTI".
- Todas las subclases (`DarkRoast`, `HouseBlend`, `Espresso`, etc.) llaman a `super().__init__(size)` en su constructor, de modo que heredan automáticamente la validación y el almacenamiento del tamaño.
- Todas las bebidas soportan los tres tamaños estándar (`TALL`, `GRANDE`, `VENTI`)
- Los decoradores (en nuestro caso solo Soy cambia costo según size) no almacenan size propio: en su lugar consultan el `get_size()` del componente envuelto. De esta manera, el estado no se duplica y se cumple el principio Open–Closed (OCP).

## Constructor de brebajes: (build_beverages):
- Para simplificar la creación de las bebidas con varios condimentos creamos una función build_beverages(base, size, condimentos)
  - base:bebida principal
  - size: (opcional) elegís el tamaño
  - condimentos: (opcional) agregás una lista con todos los condimentos
- El resultado es un objeto ya decorado, que evita escribir múltiples líneas en el main.py.


## Representación amigable: 
- Realizamos una función (pretty_description) que transforma cadenas como: 
  "Café Dark Roast, Mocha, Mocha, Crema"
	a:
  "Café Dark Roast con Double Mocha, Crema"
	para mejorar la legibilidad del código.

## Pruebas:
- Realizamos un archivo pytest para validar:
- Costos individuales de cada bebida.
- Que los resultados al sumar un condimento sean correctos. 
- Propagación correcta del tamaño (Soy varía según size).
- Funcionalidad de la función `pretty_description` para contar condimentos.
