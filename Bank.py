class Account:
    
    def __init__(self,name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def statement(self):
        print("Your current balance is Rs.{}".format(self.balance))
    
    def deposit(self, amount):
        self.balance += amount
        self.statement() #  calling function defined in same class
        
    def withdraw(self, amount):
         if self.balance - amount >= self.min_balance:
             self.balance -= amount
             self.statement()
         else:
            print ("Sorry, insufficent balance!")
            self.statement()
    
    def __del__(self):          #DESTRUCTOR - will delete object of this class on being called
        print("Account Exited")
        
class Current (Account):
    
    def __init__(self,name, balance):
        super().__init__(name, balance, min_balance= -1000)
        
    def __str__(self): # gives you proper info in you chose to print object of this class like print(X)
        return "{}'s balance is Rs.{}".format(self.name,self.balance)
    

X = Current("Rudrashish",2000)

X.statement()
X.withdraw(10000)

print(X)

             
    