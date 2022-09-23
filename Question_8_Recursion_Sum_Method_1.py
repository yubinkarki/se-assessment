new_list = []

# Function to seperate out the digits in a number.
def rec_sum(num):
    if num == 0:
        return num

    num_rem = num % 10
    new_list.append(num_rem)

    rec_sum(num//10)

    return None

rec_sum(127)

final_sum = 0

for i in new_list:
    final_sum += i

print(final_sum)
