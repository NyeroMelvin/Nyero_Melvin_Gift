#super class

class BankAccount:
    def __init__(self , account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount 
        print(f"Deposited {amount}. New balance: {self.balance}")
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount 
            print(f"Withdrawn {amount}. New balance: {self.balance}")    
            
        else:
            print('Insufficient funds.')
            
    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        
        
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        
        self.interest_rate = interest_rate # store the interest rate
        
            #Add new method for interest rate calculation
    
        def add_interest(self):
            interest = self.balance * self.interest_rate / 100
    
            #add the interest
            self.balance += interest
            print(f"Interest of {interest} added.New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit #store overdraft
            #override withdraw method to allow overdraft
    
        def withdraw(self, amount):
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f'Withdrew{amount}. New balance: {self.balance} ')
            else:
                print("Exceeded the overdraft limit")
            print("Exceeded the overdraft limit")
            
            
            
#create objects
saving = SavingAccount("SAV067468384",100000,5)
current = CurrentAccount("CA234567483",60000, 5)

#test method display
saving.display_balance()
saving.withdraw(15000)

print('lb--------------------  ')

current.display_balance()
current.withdraw(80000)
current.withdraw(20000)