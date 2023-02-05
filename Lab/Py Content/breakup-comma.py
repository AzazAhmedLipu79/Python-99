
""" 
shift + alt + a -=> multi line comment
" " => space character
x = x +1 => x+=1
 """

# Code with best practices:

""""  Input - "Give,me,a,Python,and,I,will,give,you,a,dead,body,!" """
#     Output - "Give me a Python and I will give you a dead body !"


s = "Give,me,a,Python,and,I,will,give,you,a,dead,body,!"
 

def space_comma(sentence):
    output =""
    for word in sentence:
        if(word == ","):
            output+=" "
        else:
            output+=word
    return output        

print("Input",s,"\n")
print("Output",space_comma(s))