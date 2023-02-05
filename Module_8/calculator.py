class Calculator:
    def add(self, a,b):
        return a+b 
    def sub(self, a,b):
        return a-b 
    def multiply(self, a,b):
        return a*b 
    def divide(self, a,b):
        return a/b 

    

test_calc = Calculator()

add = test_calc.add(10,5)
sub = test_calc.sub(10,5)
multiply = test_calc.multiply(10,5)
divide = test_calc.divide(10,5)


print(add,sub,multiply,divide)
