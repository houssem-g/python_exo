class Pizza:
    order_number = 0
    def __init__(self, ingredients=[]):
        __class__.order_number += 1
        self.ingredients = ingredients
        self.order_number = type(self).order_number

    @classmethod
    def garden_feast(cls):
        garden_feast_object=Pizza()
        garden_feast_object.ingredients = ["spinach", "olives", "mushroom"]
        return garden_feast_object
    @classmethod
    def meat_festival(cls):
        meat_festival_object=Pizza()
        meat_festival_object.ingredients= ["beef", "meatball", "bacon"]
        return meat_festival_object
    @classmethod
    def hawaiian(cls):
        hawaiian_object=Pizza()
        hawaiian_object.ingredients= ["ham", "pineapple"]
        return hawaiian_object
        


p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.garden_feast()
p3 = Pizza.hawaiian()
p4 = Pizza.meat_festival()
p5 = Pizza(["pepperoni", "bacon"])
my_pizza = Pizza(["cheese", "caviar", "oyster", "uranium"])


print("p1: ", p1.ingredients)
print("p2: ", p2.ingredients)
print("p3: ", p3.ingredients)
print("p4: ", p4.ingredients)
print("p5: ", p5.ingredients)
print("my_pizza: ", my_pizza.ingredients)
print("counter: ", p3.order_number)


'''
class Pizza:
    order = 0
    def __init__(self,ingredients):
        Pizza.order += 1
        self.ingredients = ingredients
        self.order_number = Pizza.order
    @staticmethod
    def hawaiian():
        return Pizza(['ham','pineapple'])
    @staticmethod
    def meat_festival():
        return Pizza(['beef','meatball','bacon'])
    @staticmethod
    def garden_feast():
        return Pizza(['spinach','olives','mushroom'])
'''