from abc import  ABC, abstractmethod
from doctest import Example


# Encapsulation
class Account:
    def __init__(self,account_id,holder_name,balance):
        self.account_id=account_id
        self.holder_name=holder_name
        self.balance=balance
    def deposit (self,amount):
        self.balance +=amount
        print(f"Deposited {amount} New balance {self.balance}")
    def withdraw(self,amount):
        # print(f"Withdraw {amount} New balance {self.balance} ")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} New Balance {self.balance}")
        else:
            print("insufficient funds iza bro")
    def check_balance(self):
        return self.balance
    def holder_name (self):
        return self.holder_name()
    def account_name (self):
        return self.account_id
# Inheritance
class Customers (Account):
    def __init__(self,account_id,holder_name,balance,phone_number):
        super().__init__(account_id,holder_name,balance)
        self.phone_number=phone_number
# Polymorphism
class Transaction():
    def __init__(self,amount):
        self.amount=amount
    def execute(self,account):
        pass
class DepositTransaction (Transaction):
    def execute(self,account):
        account.deposit(self.amount)
class WithdrawTransaction (Transaction):
    def execute(self,account):
        account.withdraw(self.amount)
# Abstraction
class Payment_system (ABC):
    @abstractmethod
    def process_transaction (self,amount):
        pass
class Mpesa_payment (Payment_system):
    def process_transaction(self,amount):
        print(f"Processing Mpesa payment of {amount}.")
# Example usage
mpesa=Mpesa_payment()
account1=Customers(1,'Alvin Kariuki',3500,+254707427850)
deposit=DepositTransaction(500)
withdraw=WithdrawTransaction(1200)
deposit.execute(account1)
withdraw.execute(account1)
print(f'Transactions complete, Balance for {account1.holder_name} is {account1.balance}')
