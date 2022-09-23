def string_occ(sent):
    target_word = "the"
    target_count = 0
    punc_list = [";",",",".","!"]

    split_sent = sent.split(" ")
    new_sent = []

    for i in split_sent:
        for word in i:
            if word in punc_list:
                new_word = i.replace(word, "")
                new_sent.append(new_word)
        new_sent.append(i)

    for items in new_sent:
        if items.lower() == target_word:
            target_count += 1

    return target_count


print(string_occ("The, is the; of the lol nice."))
