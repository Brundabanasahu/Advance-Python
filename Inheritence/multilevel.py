# class Father:
#     def skill1(self):
#         print("Father's driving skills")
# class Mother:
#     def skill2(self):
#         print("Mother's cooking skill")


# class Child (Father, Mother):
#     def skill3(self):
#         print("Baccha ka painting skills")

# c = Child()
# c.skill1()
# c.skill2()
# c.skill3()


class Father:
    def skill1(self):
        print("Father's driving skills")
class Mother:
    def skill2(self):
        print("Mother's cooking skill")


class Child (Father, Mother):
    def skill3(self):
        print("Baccha ka painting skills")

c = Child()
c.skill1()
c.skill2()
c.skill3()


