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

class User:
    def __init__(self, name, email, int_rate, balance):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate,balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"The following is {self.name}'s bank account")
        self.account.display_account_info()
        return self

adrian=User('Adrian Gosling', 'thisisanemail@email.com', .01,0)

adrian.make_deposit(500)

adrian.display_user_balance()

adrian.make_withdrawal(2000)