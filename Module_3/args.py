# def add(num1,num2):
#     return num1+num2

# print(add(num2=69, num1=11))


def multiply(*numbers):
    result = 1
    for num in numbers:
        result = result * num        
    return result

print(multiply(2,3,4,5,6,7,8))
  
  