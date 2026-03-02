class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("meow meow")

class Dog(Animal):
    def sound(self):
        print("bho bho")

class Lion(Animal):
    def sound(self):
        print("uaaa uaaa")

c = Cat()
c.sound()
print()
d = Dog()
d.sound()
print()
l = Lion()
l.sound()