'''abstract class - Restaurant 
abstract method - print("order accepted : Food is processing...")
normal method inside abstract class - print("recipt printed")'''

'''derived class - Veg, Non Veg, Seafood, fastfood - any2
normal method - print("ordered food items:")'''


from abc import ABC, abstractmethod


class Restaurant(ABC):

    @abstractmethod
    def order(self):
        print("Order accepted : Food is processing...")

    def receipt(self):
        print("Receipt printed")

class Veg(Restaurant):

    def order(self):
        print("Order accepted : Food is processing...")

    def items(self):
        print("Ordered food items: Paneer, Veg Biryani")

class NonVeg(Restaurant):

    def order(self):
        print("Order accepted : Food is processing...")

    def items(self):
        print("Ordered food items: Chicken Curry, Fish Fry")


v = Veg()
v.order()
v.receipt()
v.items()

print()srv://12subra

n = NonVeg()
n.order()
n.receipt()
n.items()