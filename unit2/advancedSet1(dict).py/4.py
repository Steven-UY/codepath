'''
return some sort of bool:

tp:
- the goal is to see if we can remove one letter from the entire message and then have the frequencies balanced out afterwards
- we are given a 0 indexed string of lowercased letters

we loop through the string and initialize all the characters with their frequencies
if all the characters match in frequency but one we return True else false
'''

def is_balanced(code):

    code_dictionary = {}
    frequency_dictionary = {}

    for char in code:
        if char not in code_dictionary:
            code_dictionary[char] = 1
        else:
            code_dictionary[char] += 1
    
    for key in code_dictionary.values():
        if key not in frequency_dictionary:
            frequency_dictionary[key] = 1
        else:
            frequency_dictionary[key] += 1
    
    if len(frequency_dictionary) == 2:
        return True
    else:
        False

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
    
