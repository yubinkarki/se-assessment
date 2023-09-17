"""
Question #8 - Sum of All Digits (Recursion)

From a given number, return the sum of all individual digits using recursion.  

Example:

Sample Input 1:
> 12345  

Sample Output 1:
> 15  
"""

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
