# class  Bank:
#     def interest(self):
#         pass
# class UPI:
#     def pay(self):
#         print("upi mode")

# class phonepay:
#     def pay(self):
#         print("phonepay mode")    


# class gpay:
#     def pay(self):
#         print("gpay mode")                    


# m=[UPI(),phonepay(),gpay()] 
# for i in m:
#     i.pay()       



class Vechicle:
    def start(self):
        pass

class bike:
    def start(self):
       print("start using kick") 
class car:
    def start(self):
        print("start using key") 
class scooty: 
    def start(self):
       print("start using button")            

s=[bike(),car(),scooty()]
for i in s:
    i.start()       