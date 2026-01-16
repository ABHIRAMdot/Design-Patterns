#Decorator Pattern
class Coffee:
    def cost(self):
        return 50
    
    def description(self):
        return "Plain coffee"
    
class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()
    
    def description(self):
        return self.coffee.description()
    

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 20
    
    def description(self):
        return self.coffee.description() + " + Milk"
    

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 30
    
    def description(self):
        return self.coffee.description() + " + Sugar"
    

coffee = Coffee()
print(coffee.description(), coffee.cost())

milk_with_co = MilkDecorator(coffee)
print(milk_with_co.description(), milk_with_co.cost())

sugar_with_co = SugarDecorator(coffee)
print(sugar_with_co.description(), sugar_with_co.cost())