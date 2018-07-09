class Pizza:
    HAM_MUSHROOM_PIZZA_TYPE = 0
    DELUXE_PIZZA_TYPE = 1
    SEAFOOD_PIZZA_TYPE = 2

    def __init__(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price


class HamAndMushroomPizza(Pizza):
    def __init__(self):
        super().__init__(8.50)


class DeluxePizza(Pizza):
    def __init__(self):
        super().__init__(10.50)


class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__(11.50)


class PizzaFactory:
    def createPizza(pizzaType):
        if pizzaType == Pizza.HAM_MUSHROOM_PIZZA_TYPE:
            print("Ham Mushroom Pizza")
            return HamAndMushroomPizza()
        elif pizzaType == Pizza.DELUXE_PIZZA_TYPE:
            print("Deluxe Pizza")
            return DeluxePizza()
        elif pizzaType == Pizza.SEAFOOD_PIZZA_TYPE:
            print("Seafood Pizza")
            return SeafoodPizza()
        else:
            return DeluxePizza()

if __name__ == '__main__':
    pizzaPrice = PizzaFactory.createPizza(Pizza.SEAFOOD_PIZZA_TYPE).getPrice()
    print(pizzaPrice)
