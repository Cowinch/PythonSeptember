from random import randint
print('\n \n ') #this line of code purely exists to space our console print one line down from the file. It just looks cleaner

class BankAccount:
    all_accounts=[]
    overdraft_fee=5
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance=self.balance+amount
        print('======================================')
        print(f'New balance after a deposit of ${amount}: ${self.balance}')
        print('======================================')
        print('')
        return self

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print('======================================')
            print(f"Cash Remaining after a withdraw of ${amount}: ${self.balance}")
            print('======================================')
            print('')
        else:
            print('======================================')
            print(f"Insufficient funds for a ${amount} withdrawal, charging a ${BankAccount.overdraft_fee} fee")
            self.balance=self.balance-BankAccount.overdraft_fee
            print(f'New total after overdraft fee: ${self.balance}')
            print('======================================')
            print('')
        return self

    def display_account_info(self):
        print('======================================')
        print("Account Info:")
        print(f'Balance: ${self.balance}')
        print(f'Interest rate: {self.int_rate*100}%')
        print('======================================')
        print('')
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance*self.int_rate)
            print('======================================')
            print(f'New remaining balance after interest of {self.int_rate*100}%: {self.balance}')
            print('======================================')
            print('')
        else:
            print('======================================')
            print('Unfortately as your funds are too low, you did not receive an increase from interest')
            print('======================================')
            print('')
        return self

    @classmethod 
    def print_all_bank_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account={}

    def make_bank_account(self, account_number, int_rate,balance):
        """This method uses an if statement to make sure when creating a bank account, there isnt already another bank account with the same name. we use account_ +account_number to generate a string in the self.account dictionary

        Args:
            account_number (string): This is a unique string used to access a specific bank account
            int_rate (number): This is the interest rate that increases the amount in the bank
            balance (number): This is the amount of money in their account
        """
        if f"account_{account_number}" not in self.account:
            self.account["account_"+account_number]=BankAccount(int_rate,balance)
            print(f'New account has been made for: {self.name}\nAccount number: {account_number} \nStarting Balance: {balance} \nStarting Interest rate: {int_rate}')
            print('')
        return self

    def make_deposit(self, account_number, amount):
        self.account["account_"+account_number].deposit(amount)
        return self

    def make_withdrawal(self,account_number, amount):
        self.account["account_"+account_number].withdraw(amount)
        return self

    def display_user_balance(self, account_number):
        print(f"The following is {self.name}'s bank account")
        self.account["account_"+account_number].display_account_info()
        return self

adrian=User('Adrian Gosling', 'thisisanemail@email.com')

adrian.make_bank_account( '001',.025,randint(1200,3600)).make_deposit('001',500).display_user_balance('001')

adrian.make_bank_account('002',.05,randint(1000,1200)).make_withdrawal('002',randint(1000,1200))
