class BankAccount:
# don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.00, balance=0.00): 
        if int_rate<0:
            self.int_rate = 0.00
        else:
            self.int_rate = int_rate * 0.01
        
        self.balance = balance
        # print(f'Balance: ${self.balance}, Rate: {self.int_rate}%')
        pass
    
    # @classmethod
    # def print_accounts(cls):
    #     # for x in cls:
    #     print(f'Balance: $')

    #     pass

    # make a deposit
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit: ${amount}, Balance: ${self.balance}')
        return(self)

    # make a withdraw
    def withdraw(self, amount):
        newBalance = self.balance - amount
        if newBalance >= 0:
            self.balance -= amount
            print(f'Withdraw: ${amount}, Balance: ${self.balance}')
        else:
            self.balance -= 5
            print(f'Insufficient funds: Charging a $5 fee, Balance: ${self.balance}')
        return(self)

    # display account info
    def display_account_info(self):
        print(f'Inquiry, Balance: ${self.balance}, Rate: {self.int_rate}')
        return(self)

    # yield interest to the account
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        self.balance = round(self.balance, 2)
        print(f'Interest Yield, Balance: ${self.balance}, Rate: {self.int_rate}')
        return(self)


# # create BankAccount instances
# accountOne = BankAccount(2, 500)
# accountTwo = BankAccount(1, 1)

# # account one transactions
# accountOne.deposit(50) .deposit(5000) .deposit(444.44) .withdraw(300) .yield_interest() .display_account_info()

# # account two transactions
# accountTwo.deposit(1000) .deposit(2000) .withdraw(500) .withdraw(100) .withdraw(5000) .withdraw(300) .yield_interest() .display_account_info()

# # using class method print all accounts
# # BankAccount.print_accounts()


class User:

    # constructor method
    def __init__ (self, userName):
        self.user_name = userName
        self.checking = BankAccount(2, 0)
        self.savings = BankAccount(2, 0)
        print(f'User: {userName}, Savings: ${self.savings.balance}, Checking: ${self.checking.balance}')
        pass

    # make deposit to user account
    def make_deposit(self, amount, acctName):
        if acctName ==  'Savings':
            print(f'Savings Deposit User: {self.user_name}, Amount: ${amount}')
            self.savings.deposit(amount)
        if acctName == 'Checking':
            print(f'Checking Deposit User: {self.user_name}, Amount: ${amount}')
            self.checking.deposit(amount)
        return(self)

    # make withdrawal to user account
    def make_withdrawal(self, amount, acctName):
        if acctName ==  'Savings':
            print(f'Savings Withdrawal User: {self.user_name}, Amount: ${amount}')
            self.savings.withdraw(amount)
        if acctName == 'Checking':
            print(f'Checking Withdrawal User: {self.user_name}, Amount: ${amount}')
            self.checking.withdraw(amount)
        return(self)


Timerson = User('Timerson')
Timerson.make_deposit(300, 'Savings')
Timerson.make_deposit(500, 'Checking')
Timerson.make_withdrawal(300, 'Savings')
Timerson.make_withdrawal(300, 'Checking')
Timerson.savings.display_account_info()
Timerson.checking.display_account_info()


    # # display name and account balance
    # def display_user_balance(self):
    #     print(f'Inquiry User: {self.user_name}, Balance: ${self.account_balance}')
    #     return(self)


