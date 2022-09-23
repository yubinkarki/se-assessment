def encoder(text_to_encode):
    """Encodes a given string and returns the final value."""
    individual_letters = list(text_to_encode)  # Converting string and storing it as a list.
    unique_letters = []
    count_list = []
    new_count_list = []
    encoded_list = []

    # Getting unique letters from the string and storing it in a list.
    for x in individual_letters:
        if x not in unique_letters:
            unique_letters.append(x)
    # print(unique_letters)

    # Storing the number of occurrence of a letter in a list.
    for y in unique_letters:
        count_list.append(text_to_encode.count(y))
    # print(count_list)

    for value in count_list:
        value = str(value+2)
        new_count_list.append(value)

    for i in range(len(new_count_list)):
        encoded_list.append(new_count_list[i] + unique_letters[i])

    final_string = "".join(encoded_list)
    return final_string


def decoder(text_to_decode):
    """Decodes the provided string and returns the final value."""
    # list = [[8, "A"], [5, "a"], [3, "X"], [14, "M"]]
    content_list = []
    numbers_list = ["0","1","2","3","4","5","6","7","8","9"]
    mixed_list = []
    i = 0
        
    while i < len(text_to_decode):
        if text_to_decode[i] in numbers_list:
            if text_to_decode[i] and text_to_decode[i+1] in numbers_list:  # Check for another number after the current number.
                join_str = int(text_to_decode[i] + (text_to_decode[i+1]))  # Can only check for 2 digit numbers.
                content_list.append(join_str)
                text_to_decode = text_to_decode[:i+1] + text_to_decode[i+2:]
            else:
                content_list.append(int(text_to_decode[i]))
        else:
            content_list.append(text_to_decode[i])
        i += 1

    for i in range(0, len(content_list), 2):  # Reducing value of numbers by 2 in every 2nd position.
        content_list[i] -= 2
        mixed_list += content_list[i] * content_list[i+1]

    final_string = "".join(mixed_list)
    return final_string


myinputencode = "AAAAAAaaaXMMMMMMMMMMMM"
myinputdecode = "8A5a3X14M"

print("Encoding 'AAAAAAaaaXMMMMMMMMMMMM':", encoder(myinputencode))
print("Decoding '8A5a3X14M':", decoder(myinputdecode))
