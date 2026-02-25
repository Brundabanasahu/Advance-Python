# class father:
#     def skill1(self):
#         print("Driving,brave")

# class mother:
#     def skill2(self):
#         print("Cooking,kind")


# class child(father,mother):
#     def skill3(self):
#         print("coding,smart")        

# c=child()
# c.skill1()
# c.skill2()
# c.skill3()



class father:
    def __init__(self):
        print("Driving,brave")

class mother:
    def __init__(self):
        print("Cooking,kind")


class child(father,mother):
    def __init__(self):
        print("coding,smart") 
        super().__init__()  
        super(father,self).__init__()
             

c=child()
