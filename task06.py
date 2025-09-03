class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance   

    def deposit(self, amount):   
        self.balance += amount

    def withdraw(self, amount):  
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Yetarli mablag yoq")

    def get_balance(self):       
        return self.balance

acc = BankAccount(100)   
acc.deposit(50)          
acc.withdraw(30)         
print(acc.get_balance()) 
