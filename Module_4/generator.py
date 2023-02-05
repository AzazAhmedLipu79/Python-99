numbers = [ 12, 45, 65, 23, 89, 78, 11]

def getNumbers (nums):
    for num in nums:
        yield num 


result = getNumbers(numbers)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print("donknow")