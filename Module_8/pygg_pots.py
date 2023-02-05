

# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposite(self,amount):
#         self.balance = self.balance + amount
#     def withdraw(self,amount):
#         self.balance = self.balance - amount


# my_bank = Bank(199)
# print(my_bank.balance)
# my_bank.deposite(201)
# print(my_bank.balance)
# my_bank.withdraw(300) 
# print(my_bank.balance)
# print(my_bank.__dict__)


""" 


class book:
    def __init__(self, bookname):
        self.bookname = bookname
    def average(self,a,b):  #method
        print((a+b)/2)

print(book("chemistrhy").bookname)





class FundRaiser_Event:
    total_amount = 0
    def __init__(self,eventName):
        self.eventName = eventName

    def donation(self, donated_money):
        self.total_amount += donated_money
        print(f'You have donated {donated_money}$ and current fund is {self.total_amount}$ ')
    def withdraw_money(self, withdrawed_money):
        self.total_amount -= withdrawed_money
        print(f'You have withdrawed {withdrawed_money}$ and {self.total_amount}$ left')
    def fund_balance(self):
        print(f'Current Fund Balance Is {self.total_amount}')


""" 
# fundraiser class -> goal -> 200$ 
# print()
#  """

# flood_fund = FundRaiser_Event("flood fund")

# flood_fund.donation(10)

# flood_fund.withdraw_money(7)

# flood_fund.donation(20)

# flood_fund.fund_balance()


# print(flood_fund.__dict__)



#  """

import random


def circle_eq(x,y,h=0,k=0):
    return ( x - h )**2 + ( y - k )**2


for number in range(100):
    circle  = circle_eq(random.randint(1,100), random.randint(1,100))
    print()