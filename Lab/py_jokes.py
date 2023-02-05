

# import uuid

# mac_address = uuid.getnode()
# print(mac_address)

# l = ["This", "is", "very", "fantastic"]


# def create_string(l):
#     output=""
#     for word in l:
#      output+=word+" "
#     return output

# print(create_string(l))




# from pyjokes import get_jokes


# def tell_some_jokes():
#     jokes = get_jokes('en','neutral')
#     for i,joke in enumerate(jokes):
#         print(i,joke, "\n")

# tell_some_jokes()






# def print_hi():
#     print("hi")

# print(print_hi()) 

# d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}


# def create_list(arr):
#     list = []
#     for key in arr:
#         list.append(key)
#         list.append(arr[key])
#     return list

# print(create_list(d))
# : words = [] for word in 




# def replace_comma_with_space(text):
#     output = ""
#     for word in s:
#             if(word == ','):
#              output += " "
#             else:
#               output += word
#     return output

# s = "I,have,been,practising,python,since,the,course,started"




# print(replace_comma_with_space(s))



# def make_upper(string): return string.upper()

# def make_capital(string): return string.capitalize()

# def make_lower(string): return string.lower()

# def testscript(): 
#     assert make_upper('my name is hello') == "MY NAME IS HELLO"
#     assert make_capital('my name is hello')== "My name is hello"
#     assert make_lower('mY NAME is HeLlo') == "my name is hello"

# replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

# #  0,1,2,3,4,5,6,7
# s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


# # while(True):
# #     replace_with[0] = replace_with[1]
# #     replace_with[2] = replace_with[3]
# #     replace_with[4] = replace_with[5]
# #     replace_with[6] = replace_with[7]

# list_s = s.split(" ")
# newString = ""


# for ReplaceWord in replace_with:
#     for word in s:
#         if(ReplaceWord == list_s.index(word)):
#             newString+= "😂😂"
#         else:
#             newString+=word

# print(newString)
# # for ReplaceWord in replace_with:
# #     for word in s:
        
# #              if(replace_with == list_s.index(word)):
# #                 print("You need to do")
# #              else:
# #                 print("Get Lost")
        
#     # print(newString)
# print(list_s.index('chief'))      




# replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
# s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

# def replaceword(string, replacewith):
#     words = string.split()
#     for i, word in enumerate(words):
#         if word in replacewith:
#             uid = replacewith.index(word)
#             words[i] = replace_with[uid+1]
#             return ' '.join(words)

# output = replaceword(s, replace_with) 
# print(output)
 

# def clean_string(text):
#     outputnor = ""
#     for word in s:
#         if(word == ':')or (word == ',') or (word =='.') or (word ==';') or (word == "-"):
#             pass
#         else:
#             outputnor += word         
#     return outputnor
    
# s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

# output = clean_string(s)
# print(output)

# https://api.weatherapi.com/v1/current.json?key=b18dc21b38f941859ba61142212808&q=Dhaka



# import requests
# import time

# def weather_data():
#     while True:
#         response = requests.get("https://api.weatherapi.com/v1/current.json?key=b18dc21b38f941859ba61142212808&q=Dhaka")
#         data = response.json()
        
#         time.sleep(30*60)
#         print(data['current'])
        
# weather_data()







# a = ['Oh', 'Emelia', 'to']

# s = "Oh I got two tickets for Dhaka. I and Emelia love visit different places very much. This time we are going to Bangladesh."

# def create_new_string():
#     output=""
#     s_list= s.split()
#     for word in a:
#         for word_s in s_list:
#             if(word == word_s):
#                 output+= s_list[s_list.index(word)+1] +" "
#             else:
#                 pass
#     return output

# with open('out.txt', 'w') as filewrite:
#     filewrite.write(create_new_string())
#     filewrite.close()














