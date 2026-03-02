from abc import ABC,abstractmethod
class vechile(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("Stpiing")
class bike(vechile):
    def start(self):
        print("bike")
class car(vechile):
    def start(self):
        print("car")


b=bike()
b.start()
b.stop()

print("")
