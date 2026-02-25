# class Animal:
#     def __init__(self):
#         print("Animal is eating")
# class dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Dog is barking")        
# class cat(dog):
#     def __init__(self):
#         super().__init__()
#         print("Cat is meowing")   

# c=cat()


class hod:
    def __init__(self):
        print("This is hod class")
class teacher(hod):
    def __init__(self):
        super().__init__()
        print("This is teacher class")
class student(teacher):
    def __init__(self):
        super().__init__()
        print("This is student class")                


s=student()        