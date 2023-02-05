# 
"""  
-prelearning
Class 
Class Method 
Class intialization(init)

-project
fundraise
fund add 
fund withdraw
fund balance check 

-finally
Task : 
 """


# Pre Learning 

# class Book:
#     def __init__(self,bookName, bookPage):
#         self.bookName = bookName
#         self.bookPage = bookPage
    

# bookPhysics = Book("Physics",321) 
# print(bookPhysics.__dict__)
 

# Project


class FundRaiser:
    def __init__(self, eventName):
        self.eventName = eventName
        self.Total_Amount = 0
    
    def donation(self, amount):
        self.Total_Amount = self.Total_Amount + amount
        print(f'Now donated {amount} and Total Fund is {self.Total_Amount}')
    
    def withdraw(self, amount):
        self.Total_Amount = self.Total_Amount - amount
        
        print(f'Now withdrawed {amount} and Total Fund is {self.Total_Amount}')
    
    def amount_check(self):
        print(f'You current Fund Is {self.Total_Amount}')
    


earth_quack_13 = FundRaiser("Earthquach 13")

earth_quack_13.donation(1000)

earth_quack_13.donation(573)

earth_quack_13.withdraw(666)

earth_quack_13.amount_check()

print(earth_quack_13.__dict__)