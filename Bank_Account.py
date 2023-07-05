# Assignment: BankAccount
# The class should also have the following methods:

    # 1 deposit(self, amount) - increases the account balance by the given amount

    # 2 withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    # 3 display_account_info(self) - print to the console: eg. "Balance: $100"

    # 4 yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
# don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance



# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon 
    
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self


    def withdraw(self, amount):
        # your code here
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self


    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")

    def yield_interest(self):
    #   your code here

        if self.balance > 0:
            self.balance *= self.int_rate + 1
        return self
        

fontella = BankAccount(0.02, 1500)

Zion = BankAccount(0.1, 2500)

BankAccount.isinstances.add()

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
fontella.deposit(700).deposit(200).deposit(900).withdraw(655).yield_interest().display_account_info()
# fontella.deposit(700 + 200 + 900).withdraw(655).yield_interest().display_account_info()


# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
Zion.deposit(600).deposit(850).withdraw(170).withdraw(40).withdraw(20).withdraw(50).yield_interest().display_account_info()

