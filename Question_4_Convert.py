def logic(my_input):
    upper_input = my_input.upper()
    list_input = list(upper_input)

    for index, words in enumerate(list_input):
        if words == " " and list_input[index-1] != " " and list_input[index+1] != " ":
            list_input[index] = "*"
    
    final_result = "".join(list_input)
    return final_result


print(logic("  Hello my friend  "))
