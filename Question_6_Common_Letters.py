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
