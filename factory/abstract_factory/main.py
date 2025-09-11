from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    ny.order_pizza("cheese")
    ny.order_pizza("veggie")
    chi.order_pizza("clam")
    chi.order_pizza("pepperoni")

if __name__ == "__main__":
    main()
