from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1)
    p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2)
    p3 = ny.order_pizza("veggie"); print("Juan ordered:", p3)
    p4 = chi.order_pizza("veggie"); print("Romina ordered:", p4)
    p5 = ny.order_pizza("pepperoni"); print("Jennifer ordered:", p5)
    p6 = chi.order_pizza("pepperoni"); print("Graciela ordered:", p6)
if __name__ == "__main__":
    main()
