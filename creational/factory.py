"""
Why use it:
1. Decoupling
2. Flexibility
3. Maintainability

When to use it:
1. When a class can't expect the class of objects, it must create.
2. When a class wants its subclasses to specify the objects it creates.
3. When you want to delegate object creation to helper subclasses.
"""

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurguerFactory:
    def create_cheese_burger(self):
        ingredients = ['bun', 'cheese', 'beef-patty']
        return Burger(ingredients)

    def create_deluxe_burger(self):
        ingredients = ['bun', 'tomato', 'lettuce', 'cheese', 'beef-patty']
        return Burger(ingredients)

    def create_vegan_burger(self):
        ingredients = ['bun', 'special-sauce', 'veggie-patty']
        return Burger(ingredients)

burger_factory = BurguerFactory()
burger_factory.create_cheese_burger().print()
burger_factory.create_deluxe_burger().print()
burger_factory.create_vegan_burger().print()
