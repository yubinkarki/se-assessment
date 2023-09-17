"""
Question #4 - Convert to Uppercase  

Take a string and convert all characters to uppercase.
Replace space by * except for any leading and trailing spaces.
Those spaces should be left as it is.

Example: (underscore means whitespace)

Sample Input 1:
> Hello_my_friend 

Sample Output 1:
> HELLO*MY*FRIEND  

Sample Input 2:
> __No_Way__

Sample Output 2:
> __NO*WAY__
"""

def logic(my_input):
    upper_input = my_input.upper()
    list_input = list(upper_input)

    for index, words in enumerate(list_input):
        if words == " " and list_input[index-1] != " " and list_input[index+1] != " ":
            list_input[index] = "*"
    
    final_result = "".join(list_input)
    return final_result


print(logic("  Hello my friend  "))
