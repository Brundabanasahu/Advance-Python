class Bank:
    def details(self):
        print("details of the customer")

class SavingAccount(Bank):
    def sav(self):
        print("This is saving account")


class CurrentAccount(Bank):
    def cur(self):
        print("This is current account")

class SalaryAccount(Bank):  
    def sal(self):
        print("This is salary account")

sal=SalaryAccount()
sal.details()
sal.sal()
print("------------------------------")

c=CurrentAccount()
c.details()
c.cur()
print("------------------------------")


s=SavingAccount()
s.details()  
s.sav()                