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
