## Decisiones de Diseño

### Extensión del Ejercicio Factory Method

Agregamos las variedades **Veggie** y **Pepperoni** siguiendo la misma lógica que las pizzas ya existentes en el patrón *Factory Method*.  
Cada estilo se implementó como una nueva clase concreta en `pizzas.py` y se actualizaron los métodos `create_pizza` en los `PizzaStore` correspondientes.  

A diferencia de la primera versión (donde las pizzas no tenían salsa explícita), ahora cada variedad incorpora también un estilo de **salsa**, que puede cambiarse a futuro.  

#### Especificaciones de las nuevas pizzas:

- **Pizza Veggie NY**  
  - Queso Reggiano vegano gratinado  
  - Champiñones  
  - Cebolla  
  - **Salsa:** Marinara  

- **Pizza Pepperoni NY**  
  - Queso Reggiano  
  - Cebolla  
  - Pepperoni  
  - **Salsa:** Marinara  

- **Pizza Veggie Chicago**  
  - Queso rallado Mozzarella vegano  
  - Aceitunas negras  
  - Espinaca  
  - Berenjena  
  - **Salsa:** Marinara  

- **Pizza Pepperoni Chicago**  
  - Queso Mozzarella  
  - Pepperoni  
  - Aceitunas negras  

---

### Extensión con Abstract Factory

- **Uso del patrón Abstract Factory**:  
  Se eligió este patrón para separar la creación de ingredientes de la lógica de preparación de pizzas.  
  Esto permite que cada `PizzaStore` (NY, Chicago, etc.) defina qué ingredientes específicos utiliza sin modificar las clases de pizzas.

- **Jerarquía de Ingredientes**:  
  Los ingredientes básicos (`Dough`, `Sauce`, `Cheese`, `Clams`) se modelaron como clases simples con un atributo `name`.  
  Para ingredientes más variados como `Veggies` y `Pepperoni`, se usaron clases abstractas que permiten extender fácilmente la lista de variedades, además permite que un mismo ingrediente se pueda utilizar en más de una pizza.

- **Clases de Pizza**:  
  Cada pizza (`CheesePizza`, `ClamPizza`, `VeggiePizza`, `PepperoniPizza`) recibe un `PizzaIngredientFactory` y, en su método `prepare`, instancia los ingredientes necesarios.  
  Esto asegura que la preparación sea coherente con el estilo de la tienda (NY vs Chicago).

- **Responsabilidad de las Tiendas**:  
  `NYPizzaStore` y `ChicagoPizzaStore` se encargan de crear las instancias correctas de pizzas.  
  De esta manera, si en el futuro se agregan otros estilos de tiendas, solo hay que implementar una nueva `PizzaStore` y su correspondiente `IngredientFactory`.

#### Desafíos Encontrados
- **Tipado de ingredientes compuestos**:  
  En la fábrica de pepperoni inicialmente se intentó devolver una lista tipada como `list[Pepperoni, Veggies]`, pero Python no lo permite directamente.  
  La solución fue devolver una lista simple (`list`) con instancias de `Pepperoni` y, opcionalmente, `Veggies`.


- **Verificación en pruebas**:  
  Para comprobar los ingredientes correctos en los tests se decidió usar `isinstance` junto con `str(...)`, ya que cada clase de ingrediente devuelve su nombre a través de `__str__`. Las pruebas verificaron:
  
    * Que `NYPizzaStore` efectivamente crea una pizza de tipo `NY Style...`.
    * Que `ChicagoPizzaStore` crea una pizza de tipo `Chicago Style...`.
    * Que una pizza de queso de NY (`CheesePizza` creada por `NYPizzaStore`) contiene los ingredientes correctos de NY (`Thin Crust Dough`).
    * Que una pizza de almejas de Chicago (`ClamPizza` creada por `ChicagoPizzaStore`) contiene los ingredientes correctos de Chicago (`Frozen Clams`).
    * Que una pizza de almejas de NY (`ClamPizza` creada por `NYPizzaStore`) contiene los ingredientes correctos de NY, en este caso `Fresh Clams`.


 

- **Extensibilidad futura**:  
  Se priorizó la facilidad para agregar nuevos estilos de pizza o nuevas familias de ingredientes sin romper el código existente. Aunque una idea a futuro, es la de extender la lógica de los ingredientes de las pizzas `Veggies` y `Pepperoni` hacia los otros ingredientes para que así se permmita tener, por ejemplo, una clase abstracta Chesse y sus subclases sean el tipo.
