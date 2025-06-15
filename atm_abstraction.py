# first we will import ABC abstract base class for using abstract class and method
from abc import ABC , abstractmethod

# creatiing abstract class named ATM
class ATM(ABC):

    @abstractmethod
    def check_balance(self):      #any class inherited this ATM class must impelment this check balance method
        pass

    @abstractmethod
    def deposit(self, amount):    #another abstract method that must be implemented in child class 
        pass

    @abstractmethod
    def withdraw(self, amount):    #another abstract method that all subclasses must implement (define)
        pass

# now we are creating concrete class BankATM wich inherit abstract class ATM and all its methods
class BankATM(ATM):
    def __init__(self):
        self._balance=1000          #proted variable _balance and initialize with 1000

    def check_balance(self):
        return f"Your current balance is :Rs.{self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance +=amount
            return f"Successfully deposited:Rs. {amount}"
        else:
            return f"Deposited amount be positive."
        
    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient Funds."
        elif amount <= 0:
            return "Withdraw amount must be positive."
        else:
            self._balance -=amount
            return f"Successfully Withdrew:Rs.{amount}"

# now creating object(instence)

user_atm=BankATM()
print(user_atm.check_balance())       #calling check_balance method

print(user_atm.deposit(5000))         #calling and using deposit method, deposit amount and print message

print(user_atm.withdraw(2000))        #calling and using withdraw method , withdraw amount and print confirmation

print(user_atm.check_balance())       #again calling check_balance method for current balance


