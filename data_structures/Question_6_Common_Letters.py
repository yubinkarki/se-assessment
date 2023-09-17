"""
Question #6 - Find Common Letters

Write a program that takes multiple strings as input.
Print the number of common letters in all the strings.
The first input n represents the number of string inputs to be taken.
Each subsequent input will be a string.
Each input should be taken in a new line.  

Example:

Sample Input 1:
> 3  
> aeiouxyz  
> aumnpez  
> nmzea  

Sample Output 1:
> 3 
"""

def logic(inputs, input_length):
    dict = {}
    h = 0

    for word in inputs:
        for letter in word:
            dict[letter] = dict.get(letter, 0) + 1

    for values in dict:
        if dict[values] > h:
            h = dict[values]

    h_key = [k for k, v in dict.items() if v == h]  # Getting key from value using list ccomprehension.
    print(h_key)

    return h


input_length = int(input())
inputs = []

for x in range(input_length):
    inputs.append(input())

print(logic(inputs, input_length))
