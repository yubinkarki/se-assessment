def string_vowels(name):
    name_char = []  # List for individual letters in the string.
    name_vowel = []  # List for vowels in the string.
    name_vowel_index = []  # List to store index of vowels from the name_char list.
    vowels = "AEIOUaeiou"

    for i in name:  # Inserting all letters from string into list.
        name_char.append(i)
    print(name_char)

    for i in range(len(name)):
        for j in vowels:
            if name[i] == j:
                name_vowel.append(name[i])  # Inserting vowel from the string into list.
                name_vowel_index.append(i)  # Inserting the index of the vowel from the string into list.
    print(name_vowel)
    print(name_vowel_index)

    # Swapping vowels in the string.
    for i in range(len(name_vowel_index)):
        if i == len(name_vowel_index)-1:  # condition to check if it is the last index of name_vowel_index list.
            name_char[name_vowel_index[i]] = name_vowel[0]  # Swapping last vowel with first one from the list.
        else:
            name_char[name_vowel_index[i]] = name_vowel[i+1]  # Swapping vowel with the next one.

    final_name = "".join(name_char)
    return final_name


myinput = "Hippopotamus"
print(string_vowels(myinput))
