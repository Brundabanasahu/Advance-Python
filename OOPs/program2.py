# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s1 = student("bulbul",20)
# s2= student("sagar",21)
# s1.display()
# s2.display()

# class employee:
#     def __init__(self,name,age,id,dept,salary):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.dept=dept
#         self.salary=salary
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("ID:",self.id)
#         print("Department:",self.dept)
#         print("Salary:",self.salary)
# e1 = employee("bulbul",20,101,"devloper",50000)
# e2= employee("sagar",20,102,"maintainces",60000)
# e3= employee("ayush",20,103,"hardware",55000)  
# e1.display()
# e2.display()
# e3.display()

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
b1 = book("Love is blind","Brundabana",300)
b2= book("god's plan","bulbul",350)
b1.display()
b2.display()        