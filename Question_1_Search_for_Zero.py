def checkzero(nums):
    # Taking numbers from the user.
    for i in range(nums):
        numbers = int(input(f"Enter number {i+1}: "))
        number_list.append(numbers)
    # print(number_list)

    new_list = [] # New list to store all numbers converted into string.
    for values in number_list:
        str_value = str(values)
        new_list.append(str_value)
    # print(new_list)

    # Tracking numbers with more than 1 digit and break them down into single strings.
    for i in range(len(new_list)):
        for value in new_list:
            if len(value) > 1:
                break_down = list(value)
                new_list.remove(value)
                new_list = new_list + break_down
            else:
                pass
    # print(new_list)

    if "0" in new_list:
        return "Yes"
    else:
        return "No"


number_list = [] # List to store all user input numbers.
n = int(input("Enter total numbers: "))
print(checkzero(n))