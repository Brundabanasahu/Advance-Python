# class Animal:
#     def make_sound(self):
#         print("Animal class")
# class Dog(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print("dog class")
# class cat(Animal):
#     def make_sound(self):
#         print("Cat class")

# c1=cat()
# c1.make_sound()
# d1=Dog()
# d1.make_sound()



class BankAccount:
    def account_type(self):
        print("This is a Bank Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account")


class SavingAccount(BankAccount):
    def account_type(self):
        print("This is a Saving Account")

class FixedDeposit(BankAccount):
    def account_type(self):
        print("This is a Fixed Deposit Account")


c=[CurrentAccount(),SavingAccount(),FixedDeposit()]
for i in c:
    i.account_type()