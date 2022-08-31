from random import randint


class BankAccount:
    all_accounts=[]
    overdraft_fee=5
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance=self.balance+amount
        print('===================')
        print(f'New balance after a deposit of ${amount}: ${self.balance}')
        print('===================')
        return self

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print('===================')
            print(f"Cash Remaining after a withdraw of ${amount}: ${self.balance}")
            print('===================')
            print('')
        else:
            print('===================')
            print(f"Insufficient funds, charging a ${BankAccount.overdraft_fee} fee")
            self.balance=self.balance-BankAccount.overdraft_fee
            print(f'New total after overdraft fee: ${self.balance}')
            print('===================')
            print('')
        return self

    def display_account_info(self):
        print('===================')
        print("Account Info:")
        print(f'Balance: ${self.balance}')
        print(f'Interest rate: {self.int_rate*100}%')
        print('===================')
        print('')
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance*self.int_rate)
            print('===================')
            print(f'New remaining balance after interest of {self.int_rate*100}%: {self.balance}')
            print('===================')
            print('')
        else:
            print('===================')
            print('Unfortately as your funds are too low, you did not receive an increase from interest')
            print('===================')
            print('')
        return self

    @classmethod 
    def print_all_bank_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

user1=BankAccount(.01,200)
user2=BankAccount(.025,400)

user1.display_account_info().deposit(randint(1,800)).deposit(12).deposit(150).withdraw(randint(1,1200)).yield_interest().display_account_info()

user2.display_account_info().deposit(randint(1,700)).deposit(55).withdraw(randint(1,750)).withdraw(randint(1,500)).withdraw(randint(1,250)).withdraw(129).yield_interest().display_account_info()

BankAccount.print_all_bank_accounts()