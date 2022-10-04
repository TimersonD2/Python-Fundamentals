
class User:

    # Every user starts with balance of 0
    account_balance = 0

    # constructor method
    def __init__ (self, userName):
        self.user_name = userName
        print(f'User: {userName}')
        pass

    # make deposit to user account
    def make_deposit(self, amount):
        self.account_balance += amount
        print(f'Deposit User: {self.user_name}, Balance: ${self.account_balance}')
        return(self)


    # make withdrawal to user account
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f'Withdrawal User: {self.user_name}, Balance: ${self.account_balance}')
        return(self)


    # display name and account balance
    def display_user_balance(self):
        print(f'Inquiry User: {self.user_name}, Balance: ${self.account_balance}')
        return(self)


    # transfer money between users
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f'Transfer From User: {self.user_name}, Amount: ${amount}, Balance: ${self.account_balance}')
        print(f'Transfer To User: {other_user.user_name}, Amount: ${amount}, Balance: ${other_user.account_balance}')
        return(self)


# Create instances of User
Eddie = User("Eddie")
Timerson = User("Timerson")
Madison = User("Madison")

# Transactions for Eddie
Eddie.make_deposit(389.77) .make_deposit(448.22) .make_deposit(5) .make_withdrawal(177) .display_user_balance()

# Transactions for Timerson
Timerson.make_deposit(100) .make_deposit(500) .make_withdrawal(75) .make_withdrawal(150) .display_user_balance()

# Transactions for Madison
Madison.make_deposit(100) .make_withdrawal(50) .make_withdrawal(25) .make_withdrawal(50) .display_user_balance()

# Transfer from Eddie to Madison
Eddie.transfer_money(Madison, 100)



