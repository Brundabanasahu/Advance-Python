"""Banking System (Using Abstraction in Module)
    Create a module named bank.py
"""
#Inside the module:
"""Abstract Method - deposit (amount )
Normal Method - show_message() => print "TRANSACTION STARTED"
Then create a child class SavingsAccount that:
"""
#Implements
"""Deposit (amount)
Create a normal method withdraw(amount)
"""

from abc import ABC, abstractmethod


class Bank(ABC):

    def show_message(self):
        print("TRANSACTION STARTED")

    @abstractmethod
    def deposit(self, amount):
        pass


class SavingsAccount(Bank):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)