you_born = input("Which year did you birth :")
current_your = input("What's the year today :")

# print(you_born, current_your)

# str to int convert 

birth_year = int(you_born)
today_year = int(current_your)

# print( type(birth_year) , type(today_year) )

your_age = today_year - birth_year
print('Your Age is : ', your_age)