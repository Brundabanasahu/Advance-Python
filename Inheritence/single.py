# class parent:
#     def show():
#         print("This is parent class")
# class child(parent):
#     def display():
#         print("This is child class")

# c=child
# c.display()
# c.show()



class Animal:
    def eat(self):
        print("Animal is eating")

class dog(Animal):
    def bark():
        print("Dog is barking")   
d=dog
d.bark()
d.eat()            
