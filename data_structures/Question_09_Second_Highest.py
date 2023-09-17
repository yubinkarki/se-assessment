"""
Question #9 - 2nd Highest Number

From an array of numbers, return the 2nd highest number.  

Example:

Sample Input 1:
> [12, 14, 15, 9, 100]  

Sample Output 1:
> 15 
"""

def second_high(num_list):
    highest = 0
    sorted_list = []

    for _ in range(len(num_list)):
        for i in num_list:
            if i > highest and i not in sorted_list:
                highest = i

        sorted_list.append(highest)
        highest = 0

    return sorted_list[1]


num_list = [34, 1, 2, 33, 45, 56]
print(second_high(num_list))
