""" F-strings, or formatted string literals, are strings in Python that are prefixed with the letter "f". They allow you to include expressions inside a string literal by enclosing them in curly braces ({}). F-strings are a convenient way to embed variables, expressions, and other types of values into a string without having to convert them to a string first. For example, you can use an f-string to print a string with a variable embedded in it:
 """

my_name = "Mr. Xyz"
my_age = 87
my_work = "Book Writter" 
timeline = 54
about_myself    = f'My name is {my_name}. And my age is {my_age}. I am a {my_work} since {timeline} years .'

print(about_myself)