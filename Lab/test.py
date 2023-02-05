import py_jokes

def testscript(): 
    assert make_upper('my name is hello') == "MY NAME IS HELLO"
    assert make_capital('my name is hello')== "My name is hello"
    assert make_lower('mY NAME is HeLlo') == "my name is hello"

""" 
Pre Learning: 

shift + Alt + a => multi line comment
space charachter = " "
We can also express x = x + 1 to  x+=1
 """


def breakup_with_comma(sentence):
    output=""
    for word in s:
        if(word == ","):
            output+=" " #space character = " " ,  output = output + " " -> output += " "
        else:
            output += word 
    return output


print(breakup_with_comma(s))

 

""" 
 Summery : This world is running by exchanging values. You must have to input somthing , if you want any output :D
 
"""