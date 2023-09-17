"""
Question #5 - Language of Pirates

A group of pirates created their own language which is different from normal English.
Write a program that takes a string as an input and prints the translated.

Pirate language:
Take the initial letter of ever word.
Move it to the end of the word.
Add "arg" at the end.

Note:  
> Punctuations should remain at the end of the word even after translation.
> Assume that punctuations won't appear anywhere other than the end of the word.
> Punctuations to be considered are ,:;?!.
> There could be multiple punctuations.(eg: Yes!!)

Example:

Sample Input 1:
> Take what you can, give nothing back. 

Sample Output 1:
> akeTarg hatwarg ouyarg ancarg, ivegarg othingnarg ackbarg. 
"""

def logic(my_input):
    punc_list = [".", ",", "!",":",";","?"]
    input_list = my_input.split(" ")
    new_list = []

    for words in input_list:
        for i, j in enumerate(words):
            if i == 0 and [char for items in input_list for char in items if char in punc_list]:  # List comprehension.
                words = words[1:] + words[0]
                words += "arg"
                new_list.append(words)

    for punc in punc_list:
        for word in input_list:
            if punc in word:
                for index, j in enumerate(word):
                    if j in punc_list:
                        word = word[1:len(word)-1] + word[0]
                        word = word + "arg"
                        word = word + j
                        new_list.append(word)

    for items in new_list:
        for x in items:
            if x in punc_list and items.index(x) < len(items) - 1:
                new_list.remove(items)

    final_result = " ".join(new_list)
    return final_result


print(logic("Take what you can, give nothing back."))
