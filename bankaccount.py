"""I wrote this to help out a classmate, so if you're here accidently, maybe don't read it ?? 
It probably won't make a lot sense :P """

class BankAccount(object):
    
    """        
    In your original function, you did:
    def __init__(self, balance):
        self.balance = 0
    if you want to initialize self.balance to 0, you do not need to pass the balance variable in.
    just put __init__(self). However, I like to pass in a balance variable so you can initialize 
    it with any balance you want.
    """
               
    def __init__(self, balance):
        self.balance = balance
    
        
                
    """I added this get_balance method because it's much easier to access the balance this way,
    if you only return it in your withdraw and deposit function, you can't access the balance 
    when you're not withdrawing or depositing. 
    """ 
        
    def get_balance(self):
        return self.balance
        
      
          
    """   
    Your original deposit and withdraw function was working okay, 
    this was just me doing it slightly differently :) 
    """
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
        else:
            print "Invalid Transaction"
            
            
            
    """Since getting the minimum account balance is also associate with BankAccount, 
    I would not create a new class for it. I would create a new class for maybe if I
    have VIPBankAccounts that have different minimum amount of something. :)   
    
    Also, I think it might be better to pass in a min_balance variable rather than hard
    coding self.balance <= 10, because you'll have more flexibility. I you want the 
    minimum balance to be 20, you wont have to go in and change your function.           
    """ 
    
    def MinimumAccountBalance (self, min_balance):
        if self.balance <= min_balance:
            print "Below Bank Minimum Account Balance"



"""
These are some print statements that help explains my program. 
I'm only a beginner as well, so my implementation might not be the best, but I hope this helps! :D 
Working towards being a better programmer as well :) 
"""


#initialize an account name MyAccount with the initial balance of 1000
MyAccount = BankAccount(1000)
print "My original balance is:", MyAccount.get_balance()

#Deposite 200 dolar into the account
MyAccount.deposit(200)
print "After depositing $200, my account balance is: ", MyAccount.get_balance()

MyAccount.withdraw(300)
print "After withdrawing $300, my account balance is: ", MyAccount.get_balance()

#Trying to withdraw more money than you have
MyAccount.withdraw(1500)

MyAccount.withdraw(900)
print "After withdrawing $900, my account balance is: ", MyAccount.get_balance()

#Test if the account has less than 10 dollars
MyAccount.MinimumAccountBalance(10)