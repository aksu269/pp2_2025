class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        print(f"{self.owner}, your balance: {self.balance}.") 
    def withdraw(self, wth):
        if (wth <= balance):    
            self.balance -= wth
            print(f"{self.owner}, your balance: {self.balance}.") 
        else:
            print(f"Insufficient balance. Your balance: {self.balance}.") 
p1 = Account("Aksu", 2000)
p1.deposit(200)