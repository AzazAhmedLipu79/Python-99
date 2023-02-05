# def cube(x):
#     return x*x*x

# cube = lambda x: x*x*x
# add = lambda x,y: x+y


numbers = [12,45,67,34,9]

twiceIt = lambda x: x *  2

number = map(twiceIt, numbers)
odd = filter(lambda x:x%2==1 , numbers)

# print(list(odd))



actors = [
    {'name': 'sakib', 'age': 34}, 
    {'name': 'manna', 'age': 50},
    {'name': 'sabana', 'age': 65},
    {'name': 'bubli', 'age': 30},
    ]

senior_artists = filter(lambda actor: actor['age'] > 35, actors )
junior_artists = filter(lambda actor: actor['age'] < 35, actors )

print(list(senior_artists))
