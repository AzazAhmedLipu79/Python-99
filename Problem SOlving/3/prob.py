""" 
Create a function exp(a, n) that returns the exponential result ( an ). Read user input a and n in a single line from the keyboard.
 """

""" 
def exp(a,n):
    return f'result is:\t{a**n}' 



input = input("enter numbers: \t")
a,n = input.split(" ")
print(exp(int(a),int(n))) """

""" 
. Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.
  2.3-4.5-1.7
 """

# input = input("enter numbers: \t")
# a,b,c = input.split('-')

# total = float(a) + float(b) + float(c)

# print( f'result is:\t{total}' )
""" 
. Write a python program to reverse every word from a given string s and output a new string. The position of words will remain the same, but their contents will be in reverse order.

s = “Programming Hero is the best”

Expected output: “gnimmargorP oreH si eht tseb”
 """

# s = "Programming Hero is the best"
# words = s.split(" ")
# output = ""
# for word in words:
#     output += word[::-1] + " "

# print(output)
""" 
4. Write a python program for the requirement below. Notice the output must be in sorted order -
Input  : x3b4U5i2
Output : bbbbiiUUUUUxxx
 """
# input = input("Input :\t")
# output = ""

# for index,words in enumerate(input): 
#    if index%2==1:
#     for i in range(int(input[index])):
#         output += input[index-1]

# changeWordList =[]

# for word in output:
#     if word.isupper():
#         if word in changeWordList:
#             pass
#         else:
#             changeWordList.append(word)
# _ = sorted(output.lower())
# store = ""
# for outputdata in _:
#     for word in changeWordList:
#         if(outputdata.upper() == word):
#             store += outputdata.upper()
#         else:
#             store += outputdata
# print(store)

""" 
9. Write a class with two instance variables X, n . Add two methods sum() and pow() to get the sum of X+n and exponential/power of Xn . """

# class Calc:
#     def __init__(self,X,n):
#         self.X = X
#         self.n = n
#     def sum(self):
#         return self.X + self.n
#     def pow(self):
#         return self.X ** self.n
# print(Calc(2,3).pow())

""" 
Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and a method which will compute the distance between those points
 """
#  tupple

# class Distance:
#   def __init__(self,(x1,y1),(x2,y2)):
#     return self

# dataX1 = input("Input X1: \t")

# dataY1 = input("Input Y1: \t")

# dataX2 = input("Input X2: \t")

# dataY2 = input("Input Y2: \t")

# class Distance:
#   def __init__(self,x1,y1,x2,y2) -> None:
#     self.x1 = int(x1)
#     self.y1 = int(y1)
#     self.x2 = int(x2)
#     self.y2 = int(y2)
#   def show_distance(self):
#     distance = ( (self.x1 - self.x2)**2 + (self.y1 - self.y2)**2 )**.5
#     return distance


# dataKey = ["X1", "Y1", "X2", "Y2"]
# dataVal =[]
# for list in dataKey:
#   value = input(f'List in {list}: \t')
#   dataVal.append(value)
# x1,y1,x2,y2 = dataVal

# print(Distance(x1,y1,x2,y2).show_distance())

# def func(arg1, arg2, arg3=4, arg4=5):
#     print(arg1, arg2, arg3, arg4)
   

# func(6, 7)
# func(4, 5, arg3=6)
# # func()
# func(3, 4, arg2=1) 
 

# with open("studentdata.txt",'r') as fileRead:
#   data = fileRead.read()
#   print(data)

""" 
8. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Input:
numbers= [10,20,10,40,50,60,70]
target=50 
Output: 3, 4

 """""" 
class targetDetect:
  def __init__(self,numbers,target) -> None:
    self.numbers = numbers
    self.target = target
  
  @property
  def result(self):
    for index,_ in enumerate(self.numbers):
      if(index < (len(self.numbers) -1) ):
        if(int(self.numbers[index]) + int(self.numbers[index+1]) == int(target)):
          print(f'{index+1},{index+1+1}')
        else:
          pass
      else:
        pass

print("Input: \n")
numbers=  input("numbers= \t")
numberList =numbers.split(",")
target = input("target= \t")

targetDetect(numberList,target).result """


""" 
Write a python program to read student_name and mark from keyboard and store the data in a text file with an unique student_id .
 """

# import uuid 

# f = open("studentdata.txt",'w') 


# stData =[]

# while True:
#      command = input("Wanna Input? y/n: \t") 
#      if(command =="y"):
#       _uid = uuid.uuid4().int
#       student_name_input = input("Input Student Name: \t")
#       student_mark_input = input("Input Student Mark: \t")
#       cs = {'_id': _uid,'student_name': student_name_input, 'student_mark': student_mark_input}
#       stData.append(cs)
#       print('🟢',stData) 

#      elif(command == "n"):
#       break
#      else:
#       print('⚠',"Wrong Input! Enter y for entry and n for close")
#       continue

# print('🔴',stData)
# f.write(str(stData))
# f.close()
""" Write a Python class to get all possible unique subsets from a set of integers."""
class SubsetMaker:
    def __init__(self, numArr):
        self.numArr = numArr
    def subsetsList(self):
        output = [[]]
        for i in self.numArr:
            output += [[i]+j for j in output]
        return output
print(SubsetMaker([4,5,6]).subsetsList())
 