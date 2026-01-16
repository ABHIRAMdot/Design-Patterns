# Builder pattern
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None

    def show(self):
        print(self.__dict__)

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun):
        self.burger.bun = bun
        return self

    def add_patty(self, patty):
        self.burger.patty = patty
        return self

    def add_cheese(self, cheese):
        self.burger.cheese = cheese
        return self

    def build(self):
        return self.burger
    

burger =( BurgerBuilder().add_bun("seasame").add_patty("chicken").add_cheese("Yes").build())

burger.show()