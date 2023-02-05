# https://docs.google.com/document/d/1GzDNUxHOWRO6mnr5vP9Bi4XHB0aiP6cgfyyFwBYy1qQ/edit

""" 
Write a program to create a function show_employee() using the following conditions - 
    It should accept the employee’s name and salary and display both using a f string.
    If the salary is missing in the function call then assign default value 9000 to salary
    If the name is missing then assign a default value anonymous

 """

# def show_employee(name = 'a',salary=9000):
#     print(name, salary)

# name ='Asd'
# salary = 55


# show_employee(name, salary)

""" 
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call. Receive the returned values and print the type. HInts: Please google how to return multiple values from a function in python
 """

# def calculation(num1, num2):
    
#     add = num1 + num2
#     sub = num1 - num2
#     return {add,sub} , [] , () 

# print(calculation(4,2))

""" 
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list

Sample Input:
list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

Sample Output:
['My', 'name', 'is', 'Bond']

 """

 
# list1 = ["M", "na", "i", "Bo"]
# list2 = ["y", "me", "s", "nd"]
 
# output=[]
# for index,list in enumerate(list1):
#     output.append(list1[index]+list2[index])


# print(output)


""" 
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order
Hints: Search google about zip() function

Sample Input: 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Sample Output:
10 400
20 300
30 200
40 100


 """ 
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse() 

# # [(10, 400), (20, 300), (30, 200), (40, 100)]
# output = list(zip(list1,list2))

# inputC = 40

# for result in output:
#     if(result[0] == inputC):
#         print(result[1])
#     else:
#         pass
""" 

Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
Hints: Search about dict() function

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

 """
# PENDING
""" 

Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary
Hints: Search about Dictionary Comprehension

Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected Output:
{'name': 'Kelly', 'salary': 8000}





We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
Write a Python program to check if value 100 exists in the following dictionary. If it is present print “present” otherwise print “not present”

Sample Dictionary:
sample_dict = {'a': 100, 'b': 200, 'c': 300}

Expected Output:
present




Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

Given Tuple:
tuple1 = (11, [22, 33], 44, 55)

Expected Output:
(11, [222, 33], 44, 55)





Counts the number of occurrences of item 50 from a tuple
Hints: Search about count() function

Given Tuple:
tuple1 = (50, 10, 60, 70, 50)

Expected Output:
2





Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set

Hints: Search about difference_update() function in set

Given Sets
set1 = {10, 20, 30}
set2 = {20, 40, 50}

Expected Output:
{10, 30}

 """


















