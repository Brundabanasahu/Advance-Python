class parent:
    def show():
        print("This is parent class")
class child(parent):
    def display():
        print("This is child class")

c=child
c.display()
c.show()
