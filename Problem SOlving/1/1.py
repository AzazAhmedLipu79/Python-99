# https://drive.google.com/file/d/1CB8jdwyJbujc3sblIyrk_wOb_DYD3Yeh/view
""" 
Suppose you have a floating number N.1 then,
Floor is the greatest integer less than or equal to N. And Ceil is the smallest
number greater than or equal to N.
Example: for 3.4 Floor is 3 and Ceil if 4.

Write a python program that takes a floating number from users using input() and
outputs both Floor and Ceil of that number. """


# num = input("Input Your Floating Value : ")
# num_floor = num[0]
# num_ceil = num[2]
# print(num_floor, num_ceil)


""" 
Write a function that takes 3 integer inputs from user and
outputs absolute values of these integers without using any
library functions.
 """
# num = input("Input Your Value : ")
# print(num[1]+num[2]+num[3])

""" 
In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
against rock, and scissors wins against paper.
Write a python program that takes two user inputs and returns who wins the game.
Sample Input:
> Player 1: rock
> Player 2: paper
Sample Output:
> Player 2 is the winner
 
 ROCK -> Scissors ->  Paper -> Rock
 
 """
# player1 = input("Rock Papper or Scissors? : ")
# player2 = input("Rock Papper or Scissors? : ")


# if player1== "Rock":
#     if player2 == "Paper":
#         print("Player 2 Winner")
#     elif player2 == "Scissors":
#         print("Player 1 is winner")
#     else :
#         print("Both Same Tieee")
# elif player1== "Paper":
#     if player2 == "Rock":
#         print("Player 1 Winner")
#     elif player2 == "Scissors":
#         print("Player 2 is winner")
#     else :
#         print("Both Same Tieee")
# elif player1== "Scissors":
#     if player2 == "Rock":
#         print("Player 2 Winner")
#     elif player2 == "Paper":
#         print("Player 1 is winner")
#     else :
#         print("Both Same Tieee")
# else:
#     print("Somthing Wrong")

""" 
Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program.
Sample:
> Enter input: 2
> 2 is positive
> -3
> -3 is negative
> “Quit”
> (stop the program)
 """

# user_input = input("Input Your Value : \t")

# if user_input == "Quit" :
#     exit()
# elif int(user_input) == 0 :
#     print(f'{user_input} is Zero')
# elif int(user_input) > 0 :
#     print(f'{user_input} is Positive')
# elif int( user_input) < 0 :
#     print(f'{user_input} is Negative')

""" 
Write a Python program which iterates the integers from 1 to 50. For multiples of three
print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
 """

# for i in range(1, 51):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("Buzz")
#   else:
#     print(i)

""" 
Write a Python program to print the first letter of your name using special character ‘*’.
Expected Output For M:
* *
* *
* * * *
* * *
* *
* *
* *
 """ 