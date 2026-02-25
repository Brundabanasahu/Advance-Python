class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)    
s1=student("bulbul",20)
# print(s1.name)
# print(s1.age)        

# modifying the attributes
# s1.name="Sagar"
# print(s1.name)
# s1.age=21
# print(s1.age)

# deleting the attributes
# del s1.age
# print(s1.age)

# adding new attributes
# s1.city="Bangalore"
# print(s1.city)