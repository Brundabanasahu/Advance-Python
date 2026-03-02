# class dog:
#     def sound(self):
#         print("dog")

# class cat:
#     def sound(self):
#         print("cat")

# def show(animal):
#     animal.sound()

# show(dog())
# show(cat())

class VegRestaurant:
    def menu(self):
        print("Paneer, Dal, Roti")

class NonVegRestaurant:
    def menu(self):
        print("Chicken, Mutton, Fish")

def show(restaurant):
    restaurant.menu()

show(VegRestaurant())
show(NonVegRestaurant())